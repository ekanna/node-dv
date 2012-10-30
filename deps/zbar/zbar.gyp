{
  "targets": [
    {
      'target_name': 'libzbar',
      'type': 'static_library',
      'include_dirs': [
        'include',
		'zbar',
		'zbar/decoder',
		'zbar/processor',
		'zbar/qrcode',
      ],
      'sources': [
        'zbar/config.c',
        'zbar/convert.c',
        'zbar/decoder.c',
        'zbar/error.c',
        'zbar/image.c',
        'zbar/img_scanner.c',
        #'zbar/jpeg.c',
        'zbar/processor.c',
        'zbar/refcnt.c',
        'zbar/scanner.c',
        #'zbar/svg.c',
        'zbar/symbol.c',
        'zbar/video.c',
        'zbar/window.c',
        'zbar/decoder/codabar.c',
        'zbar/decoder/code128.c',
        'zbar/decoder/code39.c',
        'zbar/decoder/code93.c',
        'zbar/decoder/databar.c',
        'zbar/decoder/ean.c',
        'zbar/decoder/i25.c',
        'zbar/decoder/pdf417.c',
        'zbar/decoder/qr_finder.c',
        'zbar/processor/lock.c',
        'zbar/processor/null.c',
        #'zbar/processor/posix.c',
        #'zbar/processor/win.c',
        #'zbar/processor/x.c',
		'zbar/qrcode/bch15_5.c',
        'zbar/qrcode/binarize.c',
        'zbar/qrcode/isaac.c',
        'zbar/qrcode/qrdec.c',
        'zbar/qrcode/qrdectxt.c',
        'zbar/qrcode/rs.c',
        'zbar/qrcode/util.c',
      ],
      'conditions': [
        ['OS=="win"',
          {
            'defines': [
			  '_CRT_SECURE_NO_WARNINGS',
            ],
            'include_dirs': [
              'port',
            ],
            'sources': [
              'port/win_iconv.c',
            ],
            'link_settings': {
              'libraries': [
			   '-lwinmm.lib',
              ],
            },
            'configurations': {
              'Debug': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'AdditionalOptions': [ '/TP' ]
                  },
                },
              },
              'Release': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'AdditionalOptions': [ '/TP' ]
                  },
                },
              },
            },
          }
        ]
      ]
    },
  ]
}