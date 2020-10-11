from colorit import Colors
from utils.display import print_message


class Exceptions:
    
    @staticmethod
    def check(element, flag, enabled_count, message):
        """
        Performs a check for custom logging for JMeter elements from the JMX file after validation
        @param element: the element to validate
        @param flag: flag to control the custom logging text
        @param enabled_count: the count of elements that are enabled
        @param message: default message to print
        """
        exception_list = {
            "ResultCollector": Exceptions.result_collector,
            "ResponseAssertion": Exceptions.response_assertion,
            "JSONPathAssertion": Exceptions.json_path_assertion,
            "DebugSampler": Exceptions.debug_sampler,
            "ProxyControl": Exceptions.proxy_control,
            "BeanShellSampler": Exceptions.bean_shell_sampler,
            "CookieManager": Exceptions.cookie_manager,
            "CacheManager": Exceptions.cache_manager,
            "ConfigTestElement": Exceptions.config_test_element,
            "CSVDataSet": Exceptions.csv_data_set,
            "ConstantTimer": Exceptions.constant_timer,
            "HeaderManager": Exceptions.header_manager,
            "TestAction": Exceptions.test_action,
            "Visualizer": Exceptions.jp_result_collector
        }
        # Get the exception to check from the list
        exception_check = exception_list.get(element, Exceptions.default_choice(flag, message))
        if exception_check is not None:
            # Execute the function
            exception_check(flag, enabled_count)

    @staticmethod
    def jp_result_collector(flag, enabled_count):        
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Visualizer(s) enabled.")
            print_message(message_color=Colors.white, message="Consider disabling Plugins Visualizer(s).")
        else:
            print_message(message_color=Colors.green, message=f"{enabled_count} Visualizer(s) are enabled.")


    @staticmethod
    def result_collector(flag, enabled_count):
        
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Listener(s) enabled.")
            print_message(message_color=Colors.white, message="Consider disabling Listeners.")
        else:
            print_message(message_color=Colors.green, message=f"{enabled_count} Listener(s) are enabled.")

    @staticmethod
    def response_assertion(flag, enabled_count):
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Response Assertion(s) are enabled.")
            print_message(message_color=Colors.white, message="Consider disabling Response Assertions.")
        else:
            print_message(message_color=Colors.green, message=f"{enabled_count} Response Assertion(s) are enabled.")

    @staticmethod
    def json_path_assertion(flag, enabled_count):
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} JSON Path Assertion(s) are enabled.")
            print_message(message_color=Colors.white, message="Consider disabling JSON Path Assertions.")
        else:
            print_message(message_color=Colors.green, message=f"{enabled_count} JSON Path Assertion(s) are enabled.")

    @staticmethod
    def debug_sampler(flag, enabled_count):
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Debug Sampler(s) are enabled.")
            print_message(message_color=Colors.white, message="Consider disabling Debug Samplers.")
        else:
            print_message(message_color=Colors.green, message=f"{enabled_count} Debug Sampler(s) are enabled.")

    @staticmethod
    def proxy_control(flag, enabled_count):
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} HTTP(S) Script Recorder(s) are enabled.")
            print_message(message_color=Colors.white, message="Consider disabling HTTP(S) Script Recorder(s).")
        else:
            print_message(message_color=Colors.green,
                          message=f"{enabled_count} HTTP(S) Script Recorder(s) are enabled.")

    @staticmethod
    def bean_shell_sampler(flag, enabled_count):
        if flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Bean Shell Sampler(s) are enabled.")
            print_message(message_color=Colors.white, message="Consider using JSR223 Sampler.")
        else:
            print_message(message_color=Colors.green, message=f"{enabled_count} Bean Shell Sampler(s) are enabled.")
            print_message(message_color=Colors.white, message="Consider using JSR223 Sampler.")

    @staticmethod
    def cookie_manager(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.green, message=f"{enabled_count} CookieManager added.")
            print_message(message_color=Colors.white, message="Consider adding CookieManager.")

    @staticmethod
    def cache_manager(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Cache Manager added.")
            print_message(message_color=Colors.white, message="Consider adding Cache Manager.")

    @staticmethod
    def config_test_element(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} HTTP Request Defaults added.")
            print_message(message_color=Colors.white, message="Consider adding HTTP Request Defaults.")

    @staticmethod
    def csv_data_set(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.green, message=f"{enabled_count} CSV Data Set are added.")
            print_message(message_color=Colors.white, message="Consider adding CSV Data Set.")

    @staticmethod
    def constant_timer(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Timers added.")
            print_message(message_color=Colors.white, message="Consider adding Timers.")

    @staticmethod
    def header_manager(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Header Manager are enabled.")
            print_message(message_color=Colors.white, message="Consider adding Header Manager.")

    @staticmethod
    def test_action(flag, enabled_count):
        if not flag:
            print_message(message_color=Colors.red, message=f"{enabled_count} Test Action are enabled.")
            print_message(message_color=Colors.white, message="Consider adding Test Action.")

    @staticmethod
    def default_choice(flag, message):
        if flag:
            print_message(message_color=Colors.green, message=message)
