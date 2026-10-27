{ let f = 0; if (true) { function g() { return 1; } f ||= g(); } console.log(f); }
{ let h = 0; switch (1) { case 1: function k() { return 2; } h &&= k(); break; } console.log(h); }
