let log = []
if (/* skip if */ !enabled /* feature flag */) {
  log.push('disabled')
} else {
  log.push('enabled')
}
enabled = true
log.push(enabled ? 'post' : 'pre')
console.log(log.join('|'))
