from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
search=input('Search:')
search = search.replace(" ", "%20")
driver= webdriver.Chrome()
driver.get('https://www.linkedin.com/login')
sleep(1)
driver.find_element(By.ID, 'username').send_keys('rudradebbormon@gmail.com')
sleep(1)
driver.find_element(By.ID,'password').send_keys('q4PHpXE2L%X25f2')
sleep(1)
driver.find_element(By.XPATH,"//button[@aria-label='Sign in']").click()
sleep(3)
# driver.get(f'https://www.linkedin.com/search/results/all/?keywords={search}&origin=GLOBAL_SEARCH_HEADER&sid=d7(')
# sleep(7)
driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=4234953362&keywords={search}&origin=BLENDED_SEARCH_RESULT_NAVIGATION_SEE_ALL&originToLandingJobPostings=4234953362")
sleep(3)
links=driver.find_elements(By.CLASS_NAME,"job-card-container__link")
for link in links:
    print(link.get_attribute('href'))



driver.quit()