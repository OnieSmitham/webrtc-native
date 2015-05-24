{
  'includes': [
    '../third_party/webrtc/src/webrtc/build/common.gypi',
    '../third_party/webrtc/src/talk/build/common.gypi',
    '../build/config.gypi',
    '../nodejs.gypi',
  ],
  'variables': {
    'include_tests%': 0,
    'third_party%': 'third_party',
    'configuration%': 'Release',
  }, 
  'targets': [
    {
      'target_name': 'webrtc-native',
      'type': 'loadable_module',
      'product_extension': 'node',
      'sources': [
        'Core.cc',
        'BackTrace.cc',
        'EventEmitter.cc',
        'Observers.cc',
        'ArrayBuffer.cc',
        'Module.cc',
        'PeerConnection.cc',
        'DataChannel.cc',
        'GetSources.cc',
        'GetUserMedia.cc',
        'MediaStream.cc',
        'MediaStreamTrack.cc',
        'MediaConstraints.cc',
        'Wrap.cc',
      ],      
      'defines': [
        'BUILDING_NODE_EXTENSION',
      ],
      'dependencies': [
        '<(DEPTH)/webrtc/common.gyp:webrtc_common',
        '<(DEPTH)/webrtc/webrtc.gyp:webrtc_all',
        '<(DEPTH)/third_party/libsrtp/libsrtp.gyp:libsrtp',
        '<(DEPTH)/third_party/jsoncpp/jsoncpp.gyp:jsoncpp',
        '<(DEPTH)/third_party/libyuv/libyuv.gyp:libyuv',
        '<(DEPTH)/talk/libjingle.gyp:libjingle_peerconnection',
      ],
      'include_dirs': [
        '<(nodedir)/src',
        '<(nodedir)/deps/uv/include',
        '<(nodedir)/deps/v8/include',
        '<(DEPTH)/third_party/jsoncpp/source/include',
        '<(DEPTH)/third_party/libsrtp/srtp',
        '<(DEPTH)/third_party/libyuv/include',
      ],
      'conditions': [ 
        ['OS=="linux"', {
          'defines': [
            '_LARGEFILE_SOURCE', 
            '_FILE_OFFSET_BITS=64',
          ],
          'cflags': [
            '-fPIC',
            '-Wno-deprecated-declarations',
          ],
          'conditions': [
            ['clang==1', {
              'cflags': [
                '-Wall',
                '-Wextra',
                '-Wimplicit-fallthrough',
                '-Wmissing-braces',
                '-Wreorder',
                '-Wunused-variable',
                '-Wno-address-of-array-temporary',
                '-Wthread-safety',
              ],
              'cflags_cc': [
                '-Wunused-private-field',
              ],
            }],
          ],
        }],
        ['OS=="win"', {
          'msvs_disabled_warnings': [ 
            4251,
            4530,
            4702,
            4199,
            4201,
          ],
          'libraries': [
            '-lkernel32.lib',
            '-luser32.lib',
            '-lgdi32.lib',
            '-lwinspool.lib',
            '-lcomdlg32.lib',
            '-ladvapi32.lib',
            '-lshell32.lib',
            '-lole32.lib',
            '-loleaut32.lib',
            '-luuid.lib',
            '-lodbc32.lib',
            '-l"<(nodedir)\\<(target_arch)\\node"',
          ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-Wno-deprecated-declarations',
              '-Wno-newline-eof',
              '-Wno-unknown-pragmas',
              '-Wno-unused-result',
            ],
            'DYLIB_INSTALL_NAME_BASE': '@rpath',
          },
          'libraries': [ 
            '-undefined dynamic_lookup',
            '-framework AppKit',
            '-framework QTKit',
          ],
          'defines': [
            'USE_BACKTRACE',
            '_LARGEFILE_SOURCE', 
            '_FILE_OFFSET_BITS=64',
            '_DARWIN_USE_64_BIT_INODE=1',
          ],
        }],
      ],      
    },
    {
      'target_name': 'All',
      'type': 'none',
      'dependencies': [
        'webrtc-native',
      ],
    },
  ],
}
