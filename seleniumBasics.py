from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def capture_website_content(site_info, userAgentString, headless=True, output_folder="."):
    # url非空值時繼續
    if not site_info["url"]:
        print(f"Skipping {site_info['siteName']} - URL is empty")
        return
    else:
        print(f"{site_info['siteName']}:{site_info['url']}")


    # 配置 ff 的 options
    options = Options()
    options.add_argument('--no-sandbox')
    
    # 加入 headless 控制以便在前景或後台執行
    if headless:
        options.add_argument('-headless')

    # 加入自定義的 http header(User-Agent等)
    user_agent = userAgentString
    options.set_preference("general.useragent.override", user_agent)

    # 创建Firefox WebDriver，并使用上述配置
    driver = webdriver.Firefox(options=options)

    try:
        # 開網頁
        driver.get(site_info["url"])

        # 等待直到頁面載入完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "your_target_ID"))
        )

        # 取得目標元素內容
        target_element = driver.find_element(By.ID, "your_target_ID")
        text_value = target_element.text

        # 整個網頁存檔
        # 指定存檔資料夾
        siteName = site_info['siteName'].split('(')[0].strip()
        output_path = os.path.join(output_folder, f"{siteName}{text_value}.html")
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    finally:
        # 關閉瀏覽器
        driver.quit()


# Configs
userAgentString = "your_agent_string"
headlessStat = True
outputFolder = '存檔資料夾'
sites = [
    {"siteName": "somewhere","url": "https://some.where.com"},
    {"siteName": "空url","url": ""},
]

if __name__ == "__main__":
    for site in sites:
        capture_website_content(site, userAgentString, headless=headlessStat, output_folder=outputFolder)
