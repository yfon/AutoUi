from selenium import webdriver


class GetDriver(object):

    def __new__(self, type):
        try:
            # driver = getattr(webdriver, type)()
            # driver.maximize_window()
            # driver = None
            if "Chrome" == type:
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-certificate-errors')
                driver = webdriver.Chrome(chrome_options=options)
            elif "firefox" == type:
                profile = webdriver.FirefoxProfile()
                profile.accept_untrusted_certs = True
                driver = webdriver.Firefox(firefox_profile=profile)
            else:
                capabilities = webdriver.DesiredCapabilities()
                # INTERNETE XPLORER
                capabilities['acceptSslCerts'] = True
                driver = webdriver.Ie(capabilities=capabilities)
            driver.maximize_window()
            return driver
        except:
            driver = webdriver.Chrome()
            driver.maximize_window()
            return driver
