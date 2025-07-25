from selenium import webdriver ##මේ පේළියෙන් කරන්නේ, Python program එකට Selenium library එකේ තියෙන webdriver කියන කොටස පාවිච්චි කරන්න අවසර ගන්න එක.
#webdriver කියන්නේ වෙබ් බ්‍රව්සරයක් පාලනය කරන්න අවශ්‍ය මෙවලම් තියෙන කොටස.
from selenium.webdriver.chrome.service import service, Service
#මේකෙන් කරන්නේ Selenium library එක ඇතුළේම, Chrome බ්‍රව්සරය සම්බන්ධයෙන් වැඩ කරන service කියන කොටසින් Service කියන class එක (සැකිල්ල) ගෙන්වා ගන්න එක.
#Service කියන එකෙන් තමයි අපි ChromeDriver එක කොතනද තියෙන්නේ කියලා Selenium වලට කියන්නේ.
from webdriver_manager.chrome import ChromeDriverManager
#මේ පේළිය හරිම වැදගත්! webdriver_manager කියන්නේ වෙනමම Python library එකක්.
#සාමාන්‍යයෙන් Selenium පාවිච්චි කරනකොට, Chrome බ්‍රව්සරයේ අලුත් version එකක් ආවොත්, ඒකට ගැලපෙන ChromeDriver.exe කියන පොඩි program එකත් අලුතෙන් බාගන්න ඕනේ. මේක ටිකක් කරදරකාරී වැඩක්.
#ChromeDriverManager කියන එකෙන් කරන්නේ අපිට ඒ වැඩේ කරදර වෙන්න දෙන්නේ නැතිව, අවශ්‍ය ChromeDriver.exe එක ස්වයංක්‍රීයව (automatically) බාගෙන, ඒක කොතනද තියෙන්නේ කියලා Selenium වලට කියන එක. ඒ නිසා අපිට manual විදියට ChromeDriver බාගන්න අවශ්‍ය වෙන්නේ නැහැ.

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
#මේක තමයි ප්‍රධාන පේළිය. මෙතනින් තමයි Chrome බ්‍රව්සරය විවෘත කරන්නේ.
#ChromeDriverManager().install(): මේකෙන් කරන්නේ webdriver_manager එක පාවිච්චි කරලා, අදාල Chrome version එකට ගැලපෙන ChromeDriver.exe එක බාගෙන, ඒක තියෙන තැන හොයාගන්න එක.
#Service(...): මේ Service එකට, අර හොයාගත්තු ChromeDriver.exe එකේ path එක දෙනවා.
#webdriver.Chrome(...): අන්තිමට, Selenium වලට කියනවා අර Service එක පාවිච්චි කරලා, අලුත් Chrome බ්‍රව්සර් window එකක් විවෘත කරන්න කියලා.
#driver = ...: විවෘත වුණු Chrome බ්‍රව්සරයට driver කියලා නමක් දෙනවා. දැන් අපි මේ driver කියන නම පාවිච්චි කරලා බ්‍රව්සරය පාලනය කරන්න පුළුවන්.

driver.get("http://102.130.127.112:7001/Login")
#driver කියන්නේ අපේ විවෘත වුණු Chrome බ්‍රව්සරය නේද?
#.get("..."): මේකෙන් කරන්නේ අර driver (බ්‍රව්සරය) පාවිච්චි කරලා, වරහන් ඇතුලේ දීලා තියෙන වෙබ් අඩවියේ ලිපිනයට (URL) යන්න කියලා කියන එක.
#ඉතින්, මේ කේතය ක්‍රියාත්මක වුණාම, Chrome බ්‍රව්සරය විවෘත වෙලා, http://102.130.127.112:7001/Login කියන වෙබ් අඩවියට යනවා.