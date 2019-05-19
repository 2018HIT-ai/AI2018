class bayes:
    def __init__(self):
        self.matrix = []
        self.events = None
        self.events_num = None
        self.father_num = {}
        self.fathers = {}
        self.events_CPT = {}
        self.if_caculated = {}

    def parse_father(self):
        for event in self.events:
            self.father_num[event] = 0
            self.events_CPT[event] = []
            self.fathers[event] = []
        for j in range(self.events_num):
            item = self.matrix[j]
            for i in range(self.events_num):
                if item[i] == 1:
                    self.father_num[self.events[i]] += 1
                    self.fathers[self.events[i]].append(self.events[j])

    def read_file(self, path):
        with open(path) as f:
            i = 0
            j = 0
            line = f.readline()
            i += 1
            if line: self.events_num = int(line)
            while line:
                line = f.readline()
                i += 1
                if i == 3: self.events = line.split()
                if 5 <= i < 5 + self.events_num:
                    self.matrix.append([int(x) for x in line.split()])
                if i == 5 + self.events_num:
                    self.parse_father()
                if 5 + self.events_num < i:
                    for k in range((self.father_num[self.events[j]]) ** 2 + 1):
                        self.events_CPT[self.events[j]].append([float(x) for x in line.split()])
                        line = f.readline()
                        i += 1
                        if line == '\n':
                            j += 1
                            break

    def unknow(self, prior):
        probability = 1.0
        for event in list(prior.keys()):
            fathers = self.fathers[event]
            line = ''
            for father in fathers:
                line = line + str(prior[father])
            if line == '':
                line = '0'
            temp = (self.events_CPT[event][int(line, 2)])[1 if prior[event] == 0 else 0]
            probability *= temp
        return probability

    def caculate_div(self, prior):
        events = list(prior.keys())
        max = 0
        for event in events:
            if self.events.index(event) > max:
                max = self.events.index(event)
        unkowns = []
        for i in range(max + 1):
            if self.events[i] not in events:
                unkowns.append(self.events[i])
        probability = 0
        if len(unkowns)==0:
            probability+=self.unknow(prior)
        if len(unkowns) == 1:
            for i in range(2):
                prior[unkowns[0]] = i
                probability += self.unknow(prior)
        elif len(unkowns) == 2:
            for i in range(2):
                prior[unkowns[0]] = i
                for i in range(2):
                    prior[unkowns[1]] = i
                    probability += self.unknow(prior)
        elif len(unkowns) == 3:
            for i in range(2):
                prior[unkowns[0]] = i
                for i in range(2):
                    prior[unkowns[1]] = i
                    for i in range(2):
                        prior[unkowns[2]] = i
                        probability += self.unknow(prior)
        return probability

    def caculate_result(self, member, denominator):
        member_result = member
        denominator_result = denominator
        return member_result / denominator_result

    def caculate(self, posterior, prior):
        member = list(prior.keys())
        member.append(posterior)
        post_prior = prior.copy()
        post_prior[posterior] = 1
        neg_prior = prior.copy()
        neg_prior[posterior] = 0
        post_member = self.caculate_div(post_prior)
        neg_member = self.caculate_div(neg_prior)
        denominator = self.caculate_div(prior)
        post = self.caculate_result(post_member, denominator)
        neg = self.caculate_result(neg_member, denominator)
        return [post, neg]

    def queries(self, path):
        with open(path) as f:
            line = f.readline()
            while line:
                if line != "\n":
                    problem = line
                    line = line.split("|")
                    line[0] = line[0].strip().strip("P(")
                    line[1] = line[1].strip().strip(")")
                    prior = line[1].split(",")
                    prior = [x.strip().split("=") for x in prior]
                    prior = {x[0]: int(True if x[1] == 'true' else False) for x in prior}
                    print(problem + ':' + str(self.caculate(line[0], prior)))
                line = f.readline()


mybayes = bayes()
mybayes.read_file("burglarnetwork.txt")
mybayes.queries("burglarqueries.txt")
