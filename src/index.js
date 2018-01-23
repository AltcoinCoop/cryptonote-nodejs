const addon = require('./build/Release/cryptonotejs');

const input = new Buffer("e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f", 'hex');
rs = addon.cryptonote_hash(input);

 console.log("World:",rs);  



