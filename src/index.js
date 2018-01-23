const cryptonote = require('./build/Release/cryptonotejs');

exports.cryptonote_hash = function(input) {
 	const buf = new Buffer(input, 'hex');
 	rs = cryptonote.cryptonote_hash(buf);
 	return rs
}




