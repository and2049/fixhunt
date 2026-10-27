#!/bin/sh
# Copy the shareable part of runs/ (results, reports, original and fixed programs, scan summaries) into demo/findings,
# which is committed and baked into the Docker image. Minimizer scratch directories and logs stay out.
set -e
cd "$(dirname "$0")/.."
rm -rf demo/findings && mkdir -p demo/findings
rsync -a --prune-empty-dirs --include '*-scan-*/rules/*/finding.json' --include '*-scan-*/rules/*/minimal.patch' \
  --exclude 'site/' --exclude 'check/' --exclude '*.log' --exclude 'budget.json' --exclude '*.tmp' \
  --exclude '*/*/min/' --exclude '*/*/run*/' --exclude '*/*/prog.*' --exclude '*/*/fixed2.*' \
  --exclude '*-scan-*/base/' --exclude '*-scan-*/combined/' --exclude '*-scan-*/min/' --exclude '*-scan-*/rules/*/*' runs/ demo/findings/
du -sh demo/findings
