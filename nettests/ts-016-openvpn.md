# Specification version number

2015-10-11-000

* _status_: obsolete

# Specification name

OpenVPN Client Test

# Test preconditions

Have OpenVPN installed and configured to work with at least one server and privileges to run the test as root.

# Expected impact

Ability to measure whether OpenVPN is working from the given network vantage point.

# Expected inputs

A single URL to fetch, supplied by command line argument "--url (-u)".
OpenVPN configuration file, specified by the command line argument "--openvpn-config (-c)"

# Test description

This test first launches OpenVPN and parses output to determine if it has bootstrapped. After bootstrap, it fetches the  URL specified by the --url argument using OpenVPN.

The specific string used to determine bootstrap from OpenVPN output in version
"0.0.1" is "Initialization Sequence Completed" from standard output.

# Expected output

## Parent data format

None.

## Required output data

success:
**boolean** The bootstrap status of OpenVPN (success or failure).

OpenVPN_linux --headless:
**dictionary** the parent key of OpenVPNs output that contains the keys stdout and stderr

stdout:
**string** Output produced by OpenVPNs standard output.

stderr:
**string** Error produced by OpenVPNs standard error.

body:
**string** The page body of a successful HTTP request.

failure:
**string** If failure, then the corresponding failure message.

## Data specification version number

## Semantics

```
'success' - True or False - whether OpenVPN has bootstrapped.
'body' - http page body if successfully requested.
'failure' - optional, present if there is a failure.
'l/usr/sbin/openvpn --config configfile': 
  'stdout' - Contents of standard output produced by OpenVPN.
  'stderr' - Contents of standard error produced by OpenVPN.
```

## Possible conclusions

We can determine whether or not OpenVPN is able to bootstrap, according to its output.
We can determine whether or not a given URL is reachable via OpenVPN.

## Example output sample
```
{
    "annotations": {
        "platform": "linux"
    },
    "backend_version": null,
    "bucket_date": "2016-12-12",
    "data_format_version": "0.2.0",
    "id": "05fbc0d8-ea13-4a46-937e-a69d761171a2",
    "input": null,
    "input_hashes": [],
    "measurement_start_time": "2016-12-11 19:51:00",
    "options": [
        "-c",
        "se-256b.ovpn",
        "-u",
        "khilafa.org"
    ],
    "probe_asn": "AS29073",
    "probe_cc": "RU",
    "probe_city": null,
    "probe_ip": "191.96.249.110",
    "report_filename": "2016-12-12/20161211T195056Z-RU-AS29073-openvpn_client_test-20161211T195048Z_AS29073_LFctdQRP2nAKUFGyw2vexp7Ey1ryyg9prOVrUdUdaK7vUfqw5b-0.2.0-probe.json",
    "report_id": "20161211T195048Z_AS29073_LFctdQRP2nAKUFGyw2vexp7Ey1ryyg9prOVrUdUdaK7vUfqw5b",
    "software_name": "ooniprobe",
    "software_version": "2.0.1",
    "test_helpers": {},
    "test_keys": {
        "body": "<!DOCTYPE html>\n<!--[if lt IE 7]> <html class=\"no-js ie6 oldie\" lang=\"en-US\"> <![endif]-->\n<!--[if IE 7]>    <html class=\"no-js ie7 oldie\" lang=\"en-US\"> <![endif]-->\n<!--[if IE 8]>    <html class=\"no-js ie8 oldie\" lang=\"en-US\"> <![endif]-->\n<!--[if gt IE 8]><!--> <html class=\"no-js\" lang=\"en-US\"> <!--<![endif]-->\n<head>\n<title>Attention Required! | CloudFlare</title>\n<meta charset=\"UTF-8\" />\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=Edge,chrome=1\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,maximum-scale=1\" />\n<link rel=\"stylesheet\" id=\"cf_styles-css\" href=\"/cdn-cgi/styles/cf.errors.css\" type=\"text/css\" media=\"screen,projection\" />\n<!--[if lt IE 9]><link rel=\"stylesheet\" id='cf_styles-ie-css' href=\"/cdn-cgi/styles/cf.errors.ie.css\" type=\"text/css\" media=\"screen,projection\" /><![endif]-->\n<style type=\"text/css\">body{margin:0;padding:0}</style>\n<!--[if lte IE 9]><script type=\"text/javascript\" src=\"/cdn-cgi/scripts/jquery.min.js\"></script><![endif]-->\n<!--[if gte IE 10]><!--><script type=\"text/javascript\" src=\"/cdn-cgi/scripts/zepto.min.js\"></script><!--<![endif]-->\n<script type=\"text/javascript\" src=\"/cdn-cgi/scripts/cf.common.js\"></script>\n\n\n</head>\n<body>\n  <div id=\"cf-wrapper\">\n    <div class=\"cf-alert cf-alert-error cf-cookie-error\" id=\"cookie-alert\" data-translate=\"enable_cookies\">Please enable cookies.</div>\n    <div id=\"cf-error-details\" class=\"cf-error-details-wrapper\">\n      <div class=\"cf-wrapper cf-header cf-error-overview\">\n        <h1 data-translate=\"challenge_headline\">One more step</h1>\n        <h2 class=\"cf-subheadline\"><span data-translate=\"complete_sec_check\">Please complete the security check to access</span> khilafa.org</h2>\n      </div><!-- /.header -->\n\n      <div class=\"cf-section cf-highlight cf-captcha-container\">\n        <div class=\"cf-wrapper\">\n          <div class=\"cf-columns two\">\n            <div class=\"cf-column\">\n              <div class=\"cf-highlight-inverse cf-form-stacked\">\n                <form class=\"challenge-form\" id=\"challenge-form\" action=\"/cdn-cgi/l/chk_captcha\" method=\"get\">\n  <script type=\"text/javascript\" src=\"/cdn-cgi/scripts/cf.challenge.js\" data-type=\"normal\"  data-ray=\"30fb78bd545f4e96\" async data-sitekey=\"6LfOYgoTAAAAAInWDVTLSc8Yibqp-c9DaLimzNGM\" data-stoken=\"fl5gc_M14MlvBWkagabZ2331buzai7si3RQwWaoZ2VW5hSm4wEZ8L1YKpEo4Y0i1pIz1ritxlzKjMC1447g_j_I0fPASTkKG6EZ0E_o-7GA\"></script>\n  <div class=\"g-recaptcha\"></div>\n  <noscript id=\"cf-captcha-bookmark\" class=\"cf-captcha-info\">\n    <div><div style=\"width: 302px\">\n      <div>\n        <iframe src=\"https://www.google.com/recaptcha/api/fallback?k=6LfOYgoTAAAAAInWDVTLSc8Yibqp-c9DaLimzNGM&stoken=fl5gc_M14MlvBWkagabZ2331buzai7si3RQwWaoZ2VW5hSm4wEZ8L1YKpEo4Y0i1pIz1ritxlzKjMC1447g_j_I0fPASTkKG6EZ0E_o-7GA\" frameborder=\"0\" scrolling=\"no\" style=\"width: 302px; height:422px; border-style: none;\"></iframe>\n      </div>\n      <div style=\"width: 300px; border-style: none; bottom: 12px; left: 25px; margin: 0px; padding: 0px; right: 25px; background: #f9f9f9; border: 1px solid #c1c1c1; border-radius: 3px;\">\n        <textarea id=\"g-recaptcha-response\" name=\"g-recaptcha-response\" class=\"g-recaptcha-response\" style=\"width: 250px; height: 40px; border: 1px solid #c1c1c1; margin: 10px 25px; padding: 0px; resize: none;\"></textarea>\n        <input type=\"submit\" value=\"Submit\"></input>\n      </div>\n    </div></div>\n  </noscript>\n</form>\n\n              </div>\n            </div>\n\n            <div class=\"cf-column\">\n              <div class=\"cf-screenshot-container\">\n              \n                <span class=\"cf-no-screenshot\"></span>\n              \n              </div>\n            </div>\n          </div><!-- /.columns -->\n        </div>\n      </div><!-- /.captcha-container -->\n\n      <div class=\"cf-section cf-wrapper\">\n        <div class=\"cf-columns two\">\n          <div class=\"cf-column\">\n            <h2 data-translate=\"why_captcha_headline\">Why do I have to complete a CAPTCHA?</h2>\n\n            <p data-translate=\"why_captcha_detail\">Completing the CAPTCHA proves you are a human and gives you temporary access to the web property.</p>\n          </div>\n\n          <div class=\"cf-column\">\n            <h2 data-translate=\"resolve_captcha_headline\">What can I do to prevent this in the future?</h2>\n\n            <p data-translate=\"resolve_captcha_antivirus\">If you are on a personal connection, like at home, you can run an anti-virus scan on your device to make sure it is not infected with malware.</p>\n\n            <p data-translate=\"resolve_captcha_network\">If you are at an office or shared network, you can ask the network administrator to run a scan across the network looking for misconfigured or infected devices.</p>\n          </div>\n        </div>\n      </div><!-- /.section -->\n\n      <div class=\"cf-error-footer cf-wrapper\">\n  <p>\n    <span class=\"cf-footer-item\">CloudFlare Ray ID: <strong>30fb78bd545f4e96</strong></span>\n    <span class=\"cf-footer-separator\">&bull;</span>\n    <span class=\"cf-footer-item\"><span data-translate=\"your_ip\">Your IP</span>: 94.242.57.2</span>\n    <span class=\"cf-footer-separator\">&bull;</span>\n    <span class=\"cf-footer-item\"><span data-translate=\"performance_security_by\">Performance &amp; security by</span> <a data-orig-proto=\"https\" data-orig-ref=\"www.cloudflare.com/5xx-error-landing?utm_source=error_footer\" id=\"brand_link\" target=\"_blank\">CloudFlare</a></span>\n    \n  </p>\n</div><!-- /.error-footer -->\n\n\n    </div><!-- /#cf-error-details -->\n  </div><!-- /#cf-wrapper -->\n\n  <script type=\"text/javascript\">\n  window._cf_translation = {};\n  \n  \n</script>\n\n</body>\n</html>\n",
        "failure": "unknown_failure openvpn_exited_unexpectedly",
        "success": true
    },
    "test_name": "openvpn_client_test",
    "test_runtime": 56.0091958046,
    "test_start_time": "2016-12-11 19:50:56",
    "test_version": "0.0.2"
}
```

## Expected Post-processing efforts

# Privacy considerations

OpenVPN does not seek to provide anonymity. 
An adversary can observe that a user is connecting to OpenVPN servers.
OpenVPN servers can also determine the users location.

# Packet capture considerations

This test does not capture packets by default.
