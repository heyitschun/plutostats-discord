from web3 import Web3

BLAST_RPC_URLS = [
    "https://rpc.blast.io",
    "https://rpc.ankr.com/blast",
    "https://blastl2-mainnet.public.blastapi.io",
    "https://blast.din.dev/rpc",
    "https://blast.blockpi.network/v1/rpc/public"
]

addresses = {
    "CATS_CONTRACT": Web3.to_checksum_address("0xF084962cdC640ED5c7d4e35E52929dAC06B60F7C"),
    "CATS_RESERVE": Web3.to_checksum_address("0x4eA682B94B7e13894C3d0b9afEbFbDd38CdACc3C"),
    "BLURETH_CONTRACT": Web3.to_checksum_address("0xB772d5C5F4A2Eef67dfbc89AA658D2711341b8E5"),
    "WETH_CONTRACT": Web3.to_checksum_address("0x4300000000000000000000000000000000000004")
}
