from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True,)
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/")
    print('Page opened sucessfully')

    email_text_box= page.locator('#email').fill("abc@test.com")
    page.wait_for_timeout(3000)
    enter_button = page.locator("#enterimg").click()
    page.wait_for_timeout(3000)
    first_name = page.locator("input[placeholder='First Name']").fill('Niladri')
    last_name = page.wait_for_selector("input[placeholder='Last Name']").fill('Sarkar')
    skills_dropdown = page.locator("//select[@id='Skills']")
    #skills_dropdown.select_option(label='Certifications')
    page.select_option("//select[@id='Skills']", label="Content Management Systems (CMS)")

    gender_checkbox = page.locator('//input[@value="FeMale"]')
    gender_checkbox.check()

    # if gender_checkbox.is_checked():
    #     print("Radio button checked", gender_checkbox.get_by_label)


    gender_value = page.locator("//div[@class='col-md-4 col-xs-4 col-sm-4']//input[@type='checkbox']")
    for i in range (gender_value.count()):
        gender_value.nth(i).check()
    # for i in gender_value:
    #     i.check()


    # hobby_checkbox = page.locator('//input[@value="Cricket"]')
    # hobby_checkbox.check()

    # if hobby_checkbox.is_checked():
    #     print("Hobby selected")





    page.wait_for_timeout(3000)
    print('Sucessfully executed!')

  