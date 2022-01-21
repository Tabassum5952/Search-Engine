#methods: dearch_keyword(self, s)

class search_cluster :
    def search_keyword(self, s):
        # searches for the keyword in the scraped data
        for line in open('log.txt'):
            if s in line:
                print(line)