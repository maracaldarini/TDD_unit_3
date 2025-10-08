class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.marker = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        entry = self.format()
        return len(entry.split())


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        num_words = self.count_words()
        return num_words / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        num_words_in_chunk = wpm * minutes
        formatted = self.format()
        extracted_words = formatted.split()
        if num_words_in_chunk > self.marker:
            self.marker += num_words_in_chunk
            return ' '.join(extracted_words[0:self.marker])
        elif num_words_in_chunk <= self.marker:
            if self.marker >= len(extracted_words):
                self.marker = num_words_in_chunk
                return ' '.join(extracted_words[0:self.marker])
            else:
                cap = self.marker
                self.marker += num_words_in_chunk
                if self.marker > len(extracted_words):
                    return ' '.join(extracted_words[cap:])
                else:
                    stop = self.marker
                    return ' '.join(extracted_words[cap:stop])

