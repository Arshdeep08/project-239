import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
	transaction = {
	'sender': 'Satoshi',
	'recipient': 'Mike',
	'amount': '5 ETH'
	}
	data = {
	'Block Height': 1,
	'timestamp': time(),
	'transactions': transaction,
	'Block Reward': '2.046327048499942521 ETH (2 + 0.046327048499942521)',
	'Uncles Reward': '0',
	'Difficulty': '7,293,278,291,370,357',
	'Total Difficulty': '28,070,572,181,009,216,929,429',
	'Size': '81,010 bytes',
	'Gas Used': '14,993,305(99.96%)',
	'Gas Limit': '14,999,907',
	'proof': proof,
	'previous_hash': previous_hash
	}
	chain.append(block)
	print("block information:", data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha512(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of block:", hex_hash)



block(previous_hash="No previous Hash. Since this is the first block.", proof=000)