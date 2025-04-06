import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os



class TestRealEstatePredictor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # os.pardir is basically "..", which goes back into the root directory
        project_root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        # convert the project root to a file path
        file_url = "file:///" + project_root
        # Build full path to website/RealEstatePredictor.html
        html_path = os.path.join(file_url, "website", "RealEstatePredictor.html")

        print("file path", html_path)
        cls.driver = webdriver.Firefox()
        cls.driver.get(html_path)
        cls.images = [
        "5906ChurchillMeadows.PNG",
        "3956Beacham.PNG",
        "1540Elite.PNG",
        "3761Trelawny.PNG",
        "50-7430Copenhagen.PNG"
    ]
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_re_01_image_and_estimated_value_displayed(self):
        # check if the element "picture" and "value" exists
        image = self.driver.find_element(By.ID, "picture")
        self.assertTrue(image.is_displayed(), "Picture of the house is not displayed")
        value = self.driver.find_element(By.ID, "value")
        self.assertTrue(value.is_displayed(), "Value is not displayed")

    def test_re_02_prev_button_functionality(self):
        # check if the element "prev" exists
        prev_button = self.driver.find_element(By.ID, "prev")
        self.assertTrue(prev_button.is_displayed(), "Webpage does not have the prev button")

    def test_re_03_next_button_functionality(self):
        # check if the element "next" exists
        next_button = self.driver.find_element(By.ID, "next")
        self.assertTrue(next_button.is_displayed(), "Webpage does not have the next button")

    def test_re_04_prev_wraps_to_last_image(self):
        
        images = self.__class__.images
        # simulate prev button click
        self.driver.find_element(By.ID, "prev").click()

        # check if the image loops to the last image
        src = self.driver.find_element(By.ID, "picture").get_attribute("src")
        image_src = os.path.basename(src)
        self.assertEqual(images[4], image_src, "Next button does not wrap to the last image") 

    def test_re_05_next_wraps_to_first_image(self):
        images = self.__class__.images
        # simulate next button click
        self.driver.find_element(By.ID, "next").click()

        # check if the image loops to the last image
        src = self.driver.find_element(By.ID, "picture").get_attribute("src")
        image_src = os.path.basename(src)
        self.assertEqual(images[0], image_src, "Prev button does not wrap to the first image")

    def test_re_06_comments_area_and_submit_button(self):
        comment_header = self.driver.find_element(By.ID, "comments")
        self.assertTrue(comment_header.is_displayed(), "Comments header is not displayed")

        username_box = self.driver.find_element(By.CLASS_NAME, "username")
        self.assertTrue(username_box.is_displayed(), "Username textarea is not displayed")

        comment_box = self.driver.find_element(By.CLASS_NAME, "comment")
        self.assertTrue(comment_box.is_displayed(), "Comment textarea is not displayed")

        submit_btn = self.driver.find_element(By.ID, "submit")
        self.assertTrue(submit_btn.is_displayed(), "Submit button is not displayed")

    def test_re_07_comments_displayed(self):
        username_box = self.driver.find_element(By.CLASS_NAME, "username")
        comment_box = self.driver.find_element(By.CLASS_NAME, "comment")
        submit_btn = self.driver.find_element(By.ID, "submit")

        username_box.send_keys("TestUser")
        comment_box.send_keys("Nice house!")

        submit_btn.click()
        time.sleep(1)

        # Check comment appears
        blogs_div = self.driver.find_element(By.ID, "blogs")
        blogs_text = blogs_div.text
        self.assertIn("TestUser", blogs_text, "Username does not appear in the comment section")
        self.assertIn("Nice house!", blogs_text, "Comment does not appear in the comment section")

    def test_re_08_username_first_comments_after(self):
        username_box = self.driver.find_element(By.CLASS_NAME, "username")
        comment_box = self.driver.find_element(By.CLASS_NAME, "comment")
        submit_btn = self.driver.find_element(By.ID, "submit")

        # Clear any previous text just in case
        username_box.clear()
        comment_box.clear()
        test_user = "UserTest2"
        test_comment = "This is a test comment."
        username_box.send_keys(test_user)
        comment_box.send_keys(test_comment)
        submit_btn.click()
        time.sleep(1)

        # Fetch the latest blog content
        blogs_div = self.driver.find_element(By.ID, "blogs")
        comments = blogs_div.find_elements(By.TAG_NAME, "p")

        self.assertGreater(len(comments), 0, "No comments found in the comment section")

        # Get the last (most recent) comment
        latest_comment = comments[-1].text

        # Check that it starts with username and contains the comment
        self.assertTrue(latest_comment.startswith(test_user), "Comment does not start with the username")
        comment_part = latest_comment.replace(f"{test_user}: ", "")
        self.assertEqual(test_comment, comment_part, "Comment content is missing or in wrong order")

    def test_re_09_comments_is_permanent(self):
        username_box = self.driver.find_element(By.CLASS_NAME, "username")
        comment_box = self.driver.find_element(By.CLASS_NAME, "comment")
        submit_btn = self.driver.find_element(By.ID, "submit")

        next_button = self.driver.find_element(By.ID, "next")
        prev_button = self.driver.find_element(By.ID, "prev")

        # comment on original house
        username_box.clear()
        comment_box.clear()
        username1 = "FirstUser"
        comment1 = "This comment should persist. 1"
        username_box.send_keys(username1)
        comment_box.send_keys(comment1)
        submit_btn.click()
        time.sleep(1)

        # check if the new comment is submitted properly
        blogs_div = self.driver.find_element(By.ID, "blogs")
        blogs_text = blogs_div.text

        self.assertIn(username1, blogs_text, "Username is not found after commenting.")
        self.assertIn(comment1, blogs_text, "Comment is not found after commenting.")

        # Go to the next house and comment
        next_button.click()
        username_box.clear()
        comment_box.clear()
        username2 = "SecondUser"
        comment2 = "This comment should persist. 2"
        username_box.send_keys(username2)
        comment_box.send_keys(comment2)
        submit_btn.click()
        time.sleep(1)

        # check if the comment from the fist house still exists in the second house and 
        blogs_div = self.driver.find_element(By.ID, "blogs")
        blogs_text = blogs_div.text

        self.assertNotIn(f"{username1}: {comment1}", blogs_text, "First house comment is found after switching to the second house.")
        self.assertIn(username2, blogs_text, "Username is not found after commenting.")
        self.assertIn(comment2, blogs_text, "Comment is not found after commenting.")

        # Navigate back to original house and check if comment is still displayed
        prev_button.click()
        time.sleep(1)

        blogs_div = self.driver.find_element(By.ID, "blogs")
        blogs_text = blogs_div.text

        self.assertIn(f"{username1}: {comment1}", blogs_text, "First house comment is not found after switching houses.")

        # navigate back to the second house and check if comment is still displayed
        next_button.click()
        time.sleep(1)

        blogs_div = self.driver.find_element(By.ID, "blogs")
        blogs_text = blogs_div.text

        self.assertIn(f"{username2}: {comment2}", blogs_text, "second house comment is not found after switching houses.")

    def test_re_10_allow_1000_comments(self):
        images = self.__class__.images

        for j in range(len(images)):
            # Inject 1000 comments for the current house via javascript
            self.driver.execute_script("""
                for (let i = 1; i <= 1000; i++) {
                    let username = "User" + i;
                    let comment = "Comment " + i;
                    homes[index].blogs.push(username + ": " + comment);
                    homes[index].numBlogs++;
                }
                DisplayHome();
            """)
            self.driver.find_element(By.ID, "next").click()

        # Verify comments were injected
        for j in range(len(images)):
            blogs_div = self.driver.find_element(By.ID, "blogs")
            blogs_text = blogs_div.text

            self.assertIn("User1: Comment 1", blogs_text)
            self.assertIn("User500: Comment 500", blogs_text)
            self.assertIn("User1000: Comment 1000", blogs_text)
            self.driver.find_element(By.ID, "prev").click()

    def test_re_11_textarea_cleared_after_submit(self):
        username_box = self.driver.find_element(By.CLASS_NAME, "username")
        comment_box = self.driver.find_element(By.CLASS_NAME, "comment")
        submit_btn = self.driver.find_element(By.ID, "submit")

        username_box.send_keys("ClearTestUser")
        comment_box.send_keys("Clear this after submit.")
        submit_btn.click()
        time.sleep(1)  

        # After submission, both fields should be empty
        self.assertEqual(username_box.get_attribute("value"), "", "Username textarea did not clear after submit.")
        self.assertEqual(comment_box.get_attribute("value"), "", "Comment textarea did not clear after submit.")


        

