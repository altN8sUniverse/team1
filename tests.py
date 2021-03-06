from main import *
import unittest


class WebTestCase(unittest.TestCase):

    
    def test_get_url(self):
        page ,title = get_page('http://google.com')
        self.assertEqual(
            'Google',
            title,
            msg='Title of Google should be'+title
        )
        self.assertEqual(
            BeautifulSoup,
            type(page),
            msg='Should return a BeautifulSoup instance'
        )
        external = get_external(page,'http://andela.co')
        self.assertNotIn(
            'andela.co',
            external,
            msg='External links should not include host domain'
        )


    
        
    def test_get_crawl(self):
        crawl = analyse_web('http://andela.co',"1")
        self.assertTrue((type(crawl) is dict), msg='The analyse_web function should return a dictionary and it should accept string as depth')



        
    def test_is_external(self):
        external = is_external('http://andela.co','/home')
        external2 = is_external('http://andela.co','#')
        external3 = is_external('http://andela.co','?home')
        external4 = is_external('http://andela.co','http://google.com')
        self.assertEqual(
            False,
            external,
            msg='/home is not an external link'
        )
        self.assertEqual(
            False,
            external2,
            msg='# is not an external link'
        )
        self.assertEqual(
            False,
            external3,
            msg='?home is not an external link'
        )
        self.assertEqual(
            True,
            external4,
            msg='Google.com is an external link'
        )

    




        



if __name__ == '__main__':
    unittest.main()