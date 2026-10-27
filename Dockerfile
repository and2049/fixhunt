# fixhunt dashboard + hunt/scan runtime. Generated programs run in Token Factory Sandboxes (FIXHUNT_SANDBOX=contree-always),
# so the image needs no bubblewrap; linters run inside the container on the pinned versions.
FROM oven/bun:1.4-debian

# node (Biome/ESLint and the JS syntax check), python + uv (ruff), clang-tidy 21 from apt.llvm.org with g++ for the
# standard headers (clang-tidy hunts and scans), diff, git (repository scans)
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates python3 diffutils xz-utils git g++ \
 && . /etc/os-release && curl -fsSL https://apt.llvm.org/llvm-snapshot.gpg.key -o /etc/apt/trusted.gpg.d/llvm.asc \
 && echo "deb http://apt.llvm.org/${VERSION_CODENAME}/ llvm-toolchain-${VERSION_CODENAME}-21 main" > /etc/apt/sources.list.d/llvm.list \
 && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && apt-get update \
 && apt-get install -y --no-install-recommends nodejs clang-tidy-21 clang-21 \
 && curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/usr/local/bin sh \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package.json bun.lock tsconfig.json ./
RUN bun install --frozen-lockfile
COPY src ./src
COPY tools ./tools
COPY data ./data
COPY README.md LICENSE ./
# Pre-populated findings for the demo: a pruned snapshot committed under demo/findings (runs/ itself is git-ignored).
# Refresh it with scripts/snapshot-findings.sh before deploying.
COPY demo/findings ./runs

# Warm the tool caches so the first hunt does not download anything
RUN bunx --bun @biomejs/biome --version && bunx eslint --version && uvx ruff@0.17.1 --version && clang-tidy-21 --version

# Fixers by absolute path so a cloned repository's layout cannot change what bunx resolves
ENV FIXHUNT_SANDBOX=contree-always FIXHUNT_HOST=0.0.0.0 FIXHUNT_PARALLEL=6 FIXHUNT_ESLINT=/app/node_modules/.bin/eslint FIXHUNT_BIOME=/app/node_modules/.bin/biome PORT=8731
EXPOSE 8731
CMD ["sh", "-c", "bun src/cli.ts serve --port ${PORT} --host ${FIXHUNT_HOST}"]
