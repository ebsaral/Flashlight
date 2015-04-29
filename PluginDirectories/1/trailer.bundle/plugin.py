import urllib, json, unicodedata

def results(parsed, original_query):
    query = parsed[0]

    rv = []
    for c in unicodedata.normalize('NFKC', query)):
        cat = unicodedata.category(c)[0]
        if cat in 'LN' or c in ok:
            rv.append(c)
        if cat == 'Z':  # space
            rv.append(' ')
    result = ''.join(rv).strip()
    url = "https://movielala.com/movies/%s/trailers" % result

    return {
                "title": "Get trailers of '{0}'".format(query),
                "run_args": [url],
                "html": """
                <script>
                setTimeout(function() {
                    window.location = %s
                }, 500);
                </script>
                """%(json.dumps(url)),
                "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
                "webview_links_open_in_browser": True
            }

def run(url):
    import os
    os.system('open "{0}"'.format(url))
