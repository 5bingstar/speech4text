var b = function (a, b) {
	for (var d = 0; d < b.length - 2; d += 3) {
		var c = b.charAt(d + 2),
			c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
			c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
		a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
	}
	return a
}

var tk =  function (a,TKK) {
	//console.log(a,TKK);
	for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
		var c = a.charCodeAt(f);
		128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
	}
	a = h;
	for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
	a = b(a, "+-3^+b+-f");
	a ^= Number(e[1]) || 0;
	0 > a && (a = (a & 2147483647) + 2147483648);
	a %= 1E6;
	return a.toString() + "." + (a ^ h)
}
	
//var zhtext = process.argv.splice(2).toString();
//console.log(decodeURI(zhtext));

//var tktext = process.argv.splice(3).toString();
//console.log(tktext);

var input = process.argv[2];

TKK=eval('((function(){var a\x3d812798518;var b\x3d522921571;return 419747+\x27.\x27+(a+b)})())');
res=tk(input, TKK.toString());
//res=tk(decodeURI('%E5%82%BB%E9%80%BC'), '413789.1384542795');
console.log(res);

//module.exports.b=b;
//module.exports.tk=tk;
