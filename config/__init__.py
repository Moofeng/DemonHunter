import os
import platform


VERSION = "v1.0"
BANNER = rf'''  ____                                       _   _                   _               
 |  _ \    ___   _ __ ___     ___    _ __   | | | |  _   _   _ __   | |_    ___   _ __     {VERSION} 
 | | | |  / _ \ | '_ ` _ \   / _ \  | '_ \  | |_| | | | | | | '_ \  | __|  / _ \ | '__|
 | |_| | |  __/ | | | | | | | (_) | | | | | |  _  | | |_| | | | | | | |_  |  __/ | |   
 |____/   \___| |_| |_| |_|  \___/  |_| |_| |_| |_|  \__,_| |_| |_|  \__|  \___| |_|   
                                                                                           
                                                                                           --- By Moofeng
'''
ROOT_PATH = os.getcwd()
SYSTEM = platform.system()