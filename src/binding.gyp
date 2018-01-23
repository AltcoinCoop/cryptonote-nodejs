{
    "targets": [
        {
            "target_name": "cryptonotejs",
            "sources": [
                "main.cc",
                "blake/blake.c",
                "blake/blake.h",
                "cryptonight/cryptonight.c",
                "cryptonight/cryptonight.h",
                "groestl/groestl.c",
                "groestl/groestl.h",
                "groestl/groestl_tables.h",
                "jh/jh.h",
                "jh/jh_ansi_opt64.c",
                "keccak/keccak.c",
                "keccak/keccak.h",
                "oaes/oaes_config.h",
                "oaes/oaes_lib.c",
                "oaes/oaes_lib.h",
                "skein/skein.c",
                "skein/skein.h",
                "skein/skein_port.h",
                "util/base64.h",
                "util/json.hpp"
            ],
            "include_dirs": [
                "src",
                "<!(node -e \"require('nan')\")"
            ],
            # "link_settings": {
            #     "libraries": [
            #         "-lboost_system",
            #         "-lboost_date_time",
            #     ]
            # },
            "cflags_cc!": [ "-fno-exceptions" ],
            "cflags_cc": [
                  "-std=libc++",
                  "-fexceptions"
            ],
        }
    ]
}


