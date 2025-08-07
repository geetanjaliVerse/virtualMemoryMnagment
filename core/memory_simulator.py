class MemorySimulator:
    def __init__(self, policy, num_pages=12, num_frames=4):
        self.policy = policy
        self.page_table = [[i, -1, 0] for i in range(num_pages)]
        self.frames = [-1] * num_frames
        self.frame_usage = []
        self.accesses = []
        self.index = 0
        self.faults = 0

    def load_access_file(self, accesses):
        self.accesses = accesses
        self.index = 0
        self.faults = 0
        self.page_table = [[i, -1, 0] for i in range(len(self.page_table))]
        self.frames = [-1] * len(self.frames)
        self.frame_usage = []

    def step(self):
        if self.index >= len(self.accesses):
            return None

        address = self.accesses[self.index]
        page_number = address % len(self.page_table)

        hit = self.page_table[page_number][1] != -1

        if not hit:
            self.faults += 1

            # Decide which frame to replace
            if -1 in self.frames:
                frame_to_use = self.frames.index(-1)
            else:
                if self.policy.__name__ == "Optimal":
                    # send remaining accesses for prediction
                    future_accesses = self.accesses[self.index + 1:]
                    frame_to_use = self.policy(self.frames, future_accesses, page_number)
                else:
                    frame_to_use = self.policy(self.frames, self.frame_usage, page_number)

                # Invalidate old page
                old_page = self.frames[frame_to_use]
                self.page_table[old_page][1] = -1
                self.page_table[old_page][2] = 0
                if old_page in self.frame_usage:
                    self.frame_usage.remove(old_page)

            # Assign new page
            self.frames[frame_to_use] = page_number
            self.page_table[page_number][1] = frame_to_use
            self.page_table[page_number][2] = 1

        # update usage (only LRU/FIFO need it)
        if page_number in self.frame_usage:
            self.frame_usage.remove(page_number)
        self.frame_usage.append(page_number)

        self.index += 1

        return {
            "page": page_number,
            "frame": self.page_table[page_number][1],
            "hit": hit,
            "faults": self.faults,
            "frames": list(self.frames),
            "table": [list(row) for row in self.page_table]
        }

