let log = []
if (/* skip if */ enabled /* feature flag */) {
  log.push('enabled')
} else {
  log.push('disabled')
}
enabled = true
log.push(enabled ? 'post' : 'pre')
console.log(log.join('|'))
