function f(a, b = /[-]/, ...rest) {
  console.log(arguments.length, b.source);
}
f(1, 2, 3); // Before fix: b=/[\-]/ → source='[\-]' → matches literal '-'
           // After fix : b=/[-]/   → source='[-]'   → matches range (invalid? but treated as literal '-' in some engines?)
            // Actually: in JS, [-] in char class is invalid range → throws SyntaxError
           // So we catch it to show behavioral difference via exception
