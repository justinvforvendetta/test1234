# Main network and testnet3 definitions updated for Reecoin

params = {
    'Reecoin_main': {
        'pubkey_address': 60, #chainparams.cpp
        'script_address': 85, #chainparams.cpp
        'genesis_hash': '00000dedb47da673c8a389eefd3eb68828f36b36abfc8d3408ca3ad81320fd74' #chainparams.cpp L62 
    },
    'Reecoin_test': {
        'pubkey_address': 111, #chainparams.cpp
        'script_address': 11, #chainparams.cpp
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #src/chainparams.cpp L129
    }
}