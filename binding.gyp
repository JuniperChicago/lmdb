{
    "targets": [{
        "target_name": "nlmdb"
      , "dependencies": [
            "<(module_root_dir)/deps/liblmdb.gyp:liblmdb"
        ]
      , "sources": [
            "src/nlmdb.cc"
          , "src/async.cc"
          , "src/database.cc"
          , "src/database_async.cc"
          , "src/batch.cc"
          , "src/batch_async.cc"
          , "src/iterator.cc"
          , "src/iterator_async.cc"
        ]
    }]
}