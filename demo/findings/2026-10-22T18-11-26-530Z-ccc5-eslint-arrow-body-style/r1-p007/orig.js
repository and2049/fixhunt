class C { static { console.log('static') } #x = 1; getX() { return #x; } } console.log(new C().getX());
