from selenium import webdriver
driver= webdriver.Chrome()
driver.get("http://music.baidu.com/top/new")
songlists = driver.find_element_by_id("songListWrapper").find_element_by_tag_name("ul").find_elements_by_tag_name("li")

for song in songlists:
    uptags = song.find_elements_by_class_name("up")
    print(type(uptags))
    if uptags:
        # 歌手
        singer = song.find_element_by_class_name("author_list").get_attribute("title")
        # 歌曲名
        songname = song.find_element_by_class_name("song-title").find_element_by_tag_name("a").text
        #print(songname)
        print("{:<20}: {}".format(songname,singer))
driver.quit()