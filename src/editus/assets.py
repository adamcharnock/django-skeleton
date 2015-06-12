PIPELINE_CSS = {
    'core': {
        'source_filenames': (
          'lib/uniform/*.css',
        ),
        'output_filename': 'css/core.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'core': {
        'source_filenames': (
            'bower/jquery/dist/jquery.min.js',
            'js/*.js',
        ),
        'output_filename': 'js/core.js',
    }
}
