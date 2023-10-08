import base64

#
# Hashing algorithm by SAHF, KENECTICS and DevKiD 10/08/2023 (c)
# Version: 1.0.0
#


class SAHF_512:
    # Init the class and runtime variables
    def __init__(self, h_string: str, salt: str = "1", *, difficulty: int = 1) -> None:
        self.data = h_string
        self.salt = (
            "0x" + h_string[0:2] + str(salt) + h_string[-2:]
            if salt != "0" and salt != 0
            else "1"
        )
        self.timestamp = "0x" + h_string[-2:]
        self.length = h_string.__len__()
        self.difficulty = 1 if difficulty not in {0, 1} else difficulty

    # Hash
    def hash(self) -> str:
        # Check the length of the string to avoid errors like IndexError
        if self.data.__len__() < 6:
            self.data = self.data * 6 + self.salt * 3
        i = 0
        # Shift the string of lenght of salt + timestamp
        while i <= self.salt.__len__() + self.timestamp.__len__():
            # Shift the string
            self.data = self.data[1:] + self.data[0]
            i += 1

        # split the string into 3 char
        self.data = [self.data[i : i + 3] for i in range(0, len(self.data), 3)]
        self.data = (
            self.data[0] + self.salt + self.data[1] + self.timestamp + self.data[2]
        )

        # Check if the salt is odd
        if self.salt.__len__() % 2 == 0:
            # reverse the string
            self.data = self.data[::-1]
        else:
            # Add manipulation
            self.data = (
                self.data[0 : self.salt.__len__() + 1]
                + self.data[self.salt.__len__() + 1 :]
            )

        # If salt is numric
        if self.salt.isnumeric():
            # Reverse the string
            self.data = self.data[::-1]

        # Find pattern and replace
        replace = [
            ["0", "a"],
            ["!", "Abms"],
            ["ms1", "4ac"],
            ["ms2", "4bc"],
            ["ed", "adc"],
        ]

        # Replacing from a list of pattern
        for i in replace:
            self.data = self.data.replace(i[0], i[1])

        # Create a list of patter und replace
        self.data = [self.data[i : i + 2] for i in range(0, len(self.data), 2)]
        # Reverse every second element in the list
        self.data[::2] = self.data[::2][::-1]
        self.data = (
            self.data[0 : self.salt.__len__() + 1]
            + self.data[self.salt.__len__() + 1 :]
        )

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Create a list of patter und replace
        replace = [
            ["ex", "d"],
            ["x", "3"],
            ["4", "23g6"],
            ["6", "4"],
            ["4vs", "a3d"],
            ["sa", "a03"],
            ["2d", "Ac"],
            [" ", "c"],
            [".", "1e"],
        ]

        # Replacing again with a list of pattern
        for i in replace:
            # Replace the pattern
            self.data = self.data.replace(i[0], i[1])

        # Split in 5 char
        self.data = [self.data[i : i + 5] for i in range(0, len(self.data), 5)]
        # Set all upper case if the element is odd
        self.data[::2] = [i.upper() for i in self.data[::2]]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Create a list of patter und replace
        replace = [
            ["3", "B"],
            ["1", "AsvsD"],
            ["9", "EvS"],
            ["6", "Vefs"],
            ["5", "CAS"],
            ["4", "VAS"],
            ["0", "V3ds"],
            ["$", "-"],
            ["6h", "Gb7"],
            ["2pPQ", "Ahlg0Ac2"],
            ["Ecuxsoh", "2"],
            ["v903eem", "8a"],
            ["utLxyDkOw", "XQu5Uia"],
            ["p9Z", "WXHQf"],
            ["n", "f3bLcD6Tq"],
            ["jLC95tpsFT", "gw"],
            ["BG4U", "9j"],
            ["xYv2Cb", "juPur"],
            ["1w9C0", "52k"],
            ["GpcA", "D4oE2F"],
            ["LQXrimG", "rffRTX"],
            ["bFjEL", "lUQOS"],
            ["Wyi", "MAErxQtDB"],
            ["XQvb8", "SqbqsaO3o"],
            ["CF6th", "z45vJ"],
            ["AMlbxD", "GzKixhoGq"],
            ["7USmy06", "W7m2lDPJa"],
            ["iaTPdwKTO", "V"],
            ["iNiB", "pnibAj4"],
            ["a", "TyW"],
            ["MY6BBV0IB", "B"],
            ["lJR", "2JoIgF"],
            ["KWp", "NSW2wygGz"],
            ["5m", "pGN"],
            ["J5FNR2", "hgwOxcJ9SP"],
            ["mdmxCvr", "kl7HjJ1l"],
            ["r2pD0YWL", "HHEbzb0eI"],
            ["52Yt", "sdu"],
            ["9aU0aKB", "efEaVSvXS"],
            ["U4kJ9wPz", "aZCHvRWR"],
            ["7kLgfrW", "mxjz52jVPT"],
            ["FrB1jUg", "98wmaf5LrX"],
            ["BDD9HOPt", "VJG9N"],
            ["5n5pRt", "8qZ2HA"],
            ["Kp4FJ", "ItTNP9Q"],
            ["Q4tW1nKY", "qHIDRNC"],
            ["RVlk", "T0r"],
            ["A4xFMXO", "EIGDXq"],
            ["qg801", "O5"],
            ["KqGwR", "6zMpl7yAtn"],
            ["zSQ8", "dsuCWA"],
            ["7YJk2ypR", "MyfrZXz8"],
            ["6", "W"],
            ["558vl", "3qLXMsD1F"],
            ["Y4n", "J"],
            ["mH", "Bn"],
            ["N3wl", "mo"],
            ["pti", "m03w"],
            ["PN3wFZ1Wv", "SJWVm"],
            ["p5fqDw1iLT", "CcuX"],
            ["3yj", "GuMGgcv06Y"],
            ["NanWbc", "W3"],
            ["v7AC", "p25HmvZ1r"],
            ["As", "ULXzp"],
            ["auwLHs", "E7"],
            ["UKmFb", "5BPia"],
            ["sDOMtPif", "9q6dN"],
            ["szgU4", "feBsgtT0kf"],
            ["XqOF6ab", "E5"],
            ["HjxIPpJs", "Mp3Z4"],
            ["vxcZXRA9", "lBDfdoodvN"],
            ["bn9", "gCA"],
            ["BeOXgvg", "Y0nE6e"],
            ["rc", "ARe3K"],
            ["ZWRUS1fsh", "Ksf4n"],
            ["R4MHqzhIT", "4sw0foGki"],
            ["jYDCYWhcxO", "9"],
            ["er4", "1WZuzjy"],
            ["7", "MWphgng53"],
            ["6", "clNQzU07V"],
            ["t", "vfi7Wf1"],
            ["YU", "NxbQUs2nv"],
            ["g", "L"],
            ["YwcqvoJwLq", "4a"],
            ["xKTSrJO", "GIpqxcT"],
            ["ZipKc0Oc5", "khH7M0"],
            ["fP", "SQJXsQx"],
            ["fNe5GHhF", "X"],
            ["GoIsj9XKD", "31L"],
            ["kdJQ", "fFx"],
            ["p7S", "Eyei2Nnr"],
            ["h0h", "7oQeOZczVk"],
            ["8Jk", "1XyQSfW"],
            ["f7zu6BjJ", "SNyG94pgNg"],
            ["g", "t"],
            ["fQUW5118", "A8c6FLU2"],
            ["O3Rj", "E"],
            ["MP", "oLI"],
            ["Gz4IQFY", "0VUG"],
            ["AQMrizaksx", "Kqeh3w"],
            ["88v", "tSyv"],
            ["EUF2q2Fbt", "QuGd"],
            ["2nxGdX", "cB4hi3"],
            ["RT", "Bz"],
            ["osh", "ANkF"],
            ["l", "uby2KjrUU"],
            ["Nb", "PFSdlQoK4"],
            ["cjzS6", "OPGFvHM"],
            ["kep6x0iHx7", "14sKID"],
            ["OFbRRaeEud", "FHu5"],
            ["rb5", "s3Z"],
            ["T", "XizXwH"],
            ["i9aKU", "B7wrJ0aM"],
            ["71PSYXf", "0dHmI0n"],
            ["f8", "xKoB5UUx7y"],
            ["tUER9gw2GY", "pWQLPgKPm"],
            ["RV", "xH"],
            ["qzKKZ3ccO", "sad2v"],
            ["wQfDWaxv", "vo"],
            ["gahR", "X"],
            ["IsJOA7TXAJ", "HwIci"],
            ["zk", "CLf0"],
            ["CUa4u2", "jKWgxTX"],
            ["yDOauuh", "xrCyD9Bxq"],
            ["GdF", "EabglddVE"],
            ["v46vyOLt", "yI5osQp"],
            ["M9", "9"],
            ["qftz0DD", "6m2RU"],
            ["HrkWI3WQzQ", "gyvq1Ks"],
            ["suW8XfLdR", "n"],
            ["iqIo8R", "6j3"],
            ["lRoX", "cGzp"],
            ["8u8aWvA", "20L"],
            ["1YG", "rIQsIUU"],
            ["4dUhLE", "eKvXZ"],
            ["E3D7Nr", "F5KwMiZj"],
            ["xD9", "xwsnu4WDeC"],
            ["WeD30pc", "FsUGrAZFR"],
            ["YmTPYniid", "fMU32B3"],
            ["S", "GbvS4UvS"],
            ["KRDW8", "fm7Om7zaqK"],
            ["V", "I"],
            ["IIiSt99r9", "pCJR"],
            ["8W", "Hq"],
            ["B503", "en2"],
            ["bKh", "eSXJNw9XP"],
            ["zDdJpVWBe", "buyWld"],
            ["PXJi82X", "VP7i"],
            ["LQpxdV8x", "6QRRrjh4U"],
            ["obpYP6w", "Q08efAY"],
            ["jv0jM", "C6"],
            ["rX", "vJ6"],
            ["wQQ7Hj", "ma3U2nihL"],
            ["ICD4", "qP4DYzuBvn"],
            ["pQpPpy", "lklP"],
            ["QV8FaSQvXL", "cehS4nRbNe"],
            ["y", "NBCzC5i3T"],
            ["mbi3Ww6", "7rXoPv"],
            ["zIla", "B"],
            ["0UC", "QovueXtu4"],
            ["RpcX1xU", "g"],
            ["yon", "a"],
            ["MbD87VxG", "sTwcASWnkc"],
            ["13XIdLV", "4Vy12Q7P"],
            ["Llt2UNgl9", "lQx"],
            ["Uk1", "uB"],
            ["fGUKm", "MiISRq"],
            ["aWQh", "wa1VFti5x1"],
            ["3mWZRI", "lTD"],
            ["3QQ", "OJjyL"],
            ["rl7ZYrF", "RNABQ8ZV9C"],
            ["78d7A7SC5W", "UPcqukUa"],
            ["8N8", "AwAZx"],
            ["yDk9QX", "VhhW"],
            ["TOJ", "8cN"],
            ["2", "GdN66"],
            ["Ky", "OIqyk9G"],
            ["taUQqRawVv", "lzLYFmxttl"],
            ["OEXmX", "4XQvx0uoJB"],
            ["YMV2zS5", "Q"],
            ["KTl0vX", "nJt"],
            ["1w", "3B"],
            ["VDfxQrhah", "2OhJkDTwb"],
            ["W3gnWSkyX", "4kj"],
            ["r6j", "K3yhM"],
            ["huCqdg6L", "qHIA9d3"],
            ["s8", "SB5sD"],
            ["6lN1r", "R"],
            ["k5y37NCpi", "9BO"],
            ["tancWTVrha", "Y"],
            ["s", "A"],
            ["Zo0", "4g2Aq2RzVf"],
            ["g", "zRi7aJDS6i"],
            ["nD1i4SVYZ", "cd1NpQKs"],
            ["YTs10P8XG5", "9yN"],
            ["aVOy", "samS4c"],
            ["2", "popr5wn"],
            ["hMMT", "a7qin"],
            ["Sf", "U"],
            ["83yHqcHqK", "3KLNyY"],
            ["kdks0P", "6TPNj3jCrl"],
            ["oZUFE", "jF3ciUd8Is"],
            ["55dqTPyF", "NZnX0XvtvU"],
            ["7taphg8HQ", "oiwgN6"],
            ["wUFd", "yTkyU8uc"],
            ["b6e", "y8O7F"],
            ["pLKR", "i"],
            ["6", "xJVvFe2e"],
            ["6WEBCzlA", "lYEo82DUGV"],
            ["qo0hSsXvkP", "xd3pStQ"],
            ["lA", "K2royR"],
            ["ua9EKQVTy", "a4s"],
            ["lZ", "X4EJAM"],
            ["wxb59YPuJs", "8A"],
            ["DFHoNwAuS", "dj"],
            ["Ke8IqhkuQ", "t"],
            ["7li8oyD", "hw70qmr1xE"],
            ["cVMV", "6z61gOsodP"],
            ["3Po7c", "ym"],
            ["DFDZSNtaZ", "zknO"],
            ["6", "8uBE"],
            ["t96", "seRV6D"],
            ["Jg20FS4PRf", "GLalwCDsjc"],
            ["WbxvfCpRWR", "LTFjK"],
            ["geiV", "C"],
            ["V4dCTLa", "JM05JYuY"],
            ["qhD", "mtv2bz25k"],
            ["Z0BQO4", "ejR"],
            ["CgM", "HARXZy"],
            ["AYtBlCKodw", "O0"],
            ["dZ5rX5", "HW27e"],
            ["Gj", "tteq"],
            ["QL", "hf"],
            ["s7z2FeU2pG", "gTV8FeVJZY"],
            ["3sbtIQyH", "2"],
            ["1JYjLln62J", "AdNznEKoqL"],
            ["f436OHQ2", "6W"],
            ["JesLE", "JfbO6jAlv"],
            ["YyMZ4Z", "pBo"],
            ["0", "lLx"],
            ["Jndyp9q1m", "g"],
            ["XBELl", "Ps3XHyEj"],
            ["IWPDBSY", "w"],
            ["lEiCixAzye", "jeZEffFsxw"],
            ["UvdO", "YjdSxQ"],
            ["QettH9Ps9e", "iuk2Nqq"],
            ["8IExAsr", "saNZL3w98g"],
            ["qN", "9lamnE"],
            ["sTEFrYA9U", "YXqme"],
            ["dYsBIQtbwo", "EPx5zgZe"],
            ["kiZ0Kvi", "k"],
            ["gyo5T4N", "0nMJ"],
            ["LOBAsHwrEw", "rZ"],
            ["1", "42jAW68"],
            ["HDVgA6yZNm", "VHfy"],
            ["NHFJ15vM", "7Y7dlul"],
            ["vz0TdSaMtV", "2eL9aVbr"],
            ["jtQ517dB", "ps9"],
            ["kzpu6F", "3P5"],
            ["RPgPaB", "oke4"],
            ["NR3wFHFGS", "h2YrZSa"],
            ["4bR6jno", "KrYIw"],
            ["clmL8", "8PaWJXprb"],
            ["fIfYY", "tIsc"],
            ["zYzcpB71AY", "f66zHE"],
            ["v", "U"],
            ["W3wFUJK7d", "LQ2ZWhy"],
            ["FPUban", "fqM"],
            ["jvAPpMyCN", "mjiMh"],
            ["3XoTS", "d"],
            ["u2Pxrulu", "YBZdlr9KqN"],
            ["qWi", "7cZ"],
            ["W6FIzkkxC", "tbD3"],
            ["mLixz", "V"],
            ["L", "TYhJBQl0nO"],
            ["6bFRQVQq", "uSjDv"],
            ["9bSXPefGM", "3YGtS"],
            ["i", "f2gKANYz"],
            ["Fwo2ohxg7", "HM51mKy4i2"],
            ["ybt39u8eW", "c"],
            ["Io", "vbuYgi"],
            ["2J8Dc", "Yt"],
            ["150c", "moF6"],
            ["jbc3P", "23"],
            ["2qr", "U"],
            ["Hc2IM0t", "580HKS"],
            ["JAUQ75v82", "mwJL"],
            ["3jgID29", "uvkcT"],
            ["4dM26zwdt", "2jco"],
            ["wsdXZj", "rTZVLdQm7"],
            ["gnrGj5oy", "en"],
            ["Okhth", "2yqj"],
            ["e", "nrv8HqY"],
            ["At3WHj87U", "0"],
            ["YpQPU9eW", "s0JAUK8"],
            ["hxO", "Q"],
            ["Uvxj3cP", "em"],
            ["FcMDIQn", "NMqiL"],
            ["ts2VVSSB", "BgdAh8"],
            ["2D", "lOVwH7Zi"],
            ["Z89g", "sq4tl"],
            ["TIK", "499vSx"],
            ["Gq9eYrU", "B"],
            ["voZe", "VGOXpui9"],
            ["8RpRb0", "K"],
            ["ZZmEOko2d", "t"],
            ["SBPDDotTY", "CryvGw4QuW"],
            ["kBgMOt", "59Wfiw8UP2"],
            ["M", "7719"],
            ["TDwRhWrVE", "8d1ZaGH0y"],
            ["74TStc6", "zTIpKtFG0"],
            ["rXT", "Qs521N6"],
            ["KDQUITgebE", "bAvlHQXkr"],
            ["w", "Pg4XjR1stQ"],
            ["c1YOCSxFEo", "xEJE7"],
            ["RSQTUyOA", "7SjYTZHMV"],
            ["Cpps1", "1GmX"],
            ["5dphU", "lV"],
            ["L0R", "kIzdth"],
            ["zNU", "iTSWFIqrib"],
            ["S1HmV4X", "O8lcpdLqX"],
            ["QC", "vH"],
            ["6zmWQ", "qTtIUi7ho"],
            ["6AIWZto9", "o5fB4cfP"],
            ["zYM", "t4xLk"],
            ["E", "cF3yI"],
            ["NX", "IoLfStYxQy"],
            ["4MNCbF", "kU3cFuE"],
            ["dOzIK", "4iDkFsE"],
            ["l", "mAvs6Mz4v4"],
            ["OjylA0O", "6ShUDz"],
            ["0s15tJk3L", "BSCyWII"],
            ["WGR", "QD6"],
            ["4hAG5Qbd", "6mWDrTHzj"],
            ["tulGvO", "LfOp"],
            ["SmtfA", "MunBg6XLi"],
            ["pk0mgH10", "2ek95o"],
            ["55Xe85vy69", "Il1HZPzJ"],
            ["exbK3", "1mojGW"],
            ["gwkvCrTMO", "i3YcSf"],
            ["0lUSEICI", "kR6uDvR7N"],
            ["NTYLze", "sA"],
            ["cg", "EHQW59"],
            ["wgQshtI", "oaS"],
            ["t", "K1DMa"],
            ["H", "W"],
            ["uzfduSLR5e", "Z"],
            ["JbiiK35Df", "AJRrgjKrb"],
            ["njOX6", "cYUCWtXGhR"],
            ["4Bw", "USgntL"],
            ["NQY3XKI", "O"],
            ["h", "VrAEo04Wg"],
            ["wIKzSLBN", "eVAL"],
            ["4", "1bbpz"],
            ["NnQ", "q"],
            ["pn", "Vnz"],
            ["mj", "UWRB9BnFf6"],
            ["JN1SA0Zv", "6ms"],
            ["weSSdMPXj", "C"],
            ["n", "wM1R"],
            ["hU4wIW6u", "8"],
            ["dL1hlV", "svosY1aP"],
            ["Z", "mWwow3Mp"],
            ["mlte25RvqU", "D44Kn"],
            ["OXoT", "tx0SDHaS8"],
            ["DmxBSJC76", "S70lvIS"],
            ["R3", "4wION5M"],
            ["xrUszj", "b"],
            ["numRfv103w", "JsNg"],
            ["seFAY", "m"],
            ["yywig", "0TPrep2B"],
            ["FMY4Yz8U", "AjA"],
            ["3X7", "vvcarHS"],
            ["puvoU0gc5e", "FRw"],
            ["z8", "zdSwAy"],
            ["VLYOsp", "ZPD5md"],
            ["5Ms", "cK6QoYgr"],
            ["YKAdTySYC", "RRHIEDOc"],
            ["v", "BTOl3"],
            ["3", "Xs"],
            ["7WUW", "rgGZOR6GJL"],
            ["xCtR", "LplqmPyeA"],
            ["OI0verq4e", "bso3f0SGQC"],
            ["JmDJF1Wkt", "P2u2bwlf"],
            ["qASecp", "U"],
            ["JA3HRmW", "XtO4csGzF"],
            ["qiUPEECEIu", "uzN8Gg9o0t"],
            ["K", "LJBJc"],
            ["w", "uduga5cqTo"],
            ["M", "8"],
            ["dLPkw", "5QSsp"],
            ["oWdfzq", "0NG9SGq"],
            ["oAEiwKr", "aezfpJgrCB"],
            ["Ka0Kikq", "BTfikT"],
            ["EbsI", "CevZXGjU"],
            ["b3WFYudjaD", "hlYkOzqL"],
            ["t4BRZ", "y162Wt7i1"],
            ["FUswt2v", "lu5V"],
            ["5Cu90Crlt", "KhtiD"],
            ["VoMTk0t", "J2X"],
            ["4SuEqrtGVn", "pDGLgvPf"],
            ["gmFW1Kt2lO", "Y"],
            ["p3naZYmcld", "xf08mk1OE"],
            ["6RTUA", "IZSQo5v93"],
            ["TGhO2p", "6A4EHBoRG"],
            ["nSKRRzG6PB", "H3UpJX4l"],
            ["YAh9tTCxzp", "sR7vt"],
            ["C2f", "s"],
            ["JG5pfF", "HDNE"],
            ["hIsK9j", "t2d44f"],
            ["s", "IGaQ"],
            ["siV", "Nl"],
            ["4Svz7VkOj", "XvIQ1"],
            ["dEtYGJy", "8idlB"],
            ["Tr5EU4SA3", "k6"],
            ["gQKNwCmj", "V"],
            ["9jPiM96t72", "o3aY"],
            ["weYAbKO", "VW"],
            ["chMTLb95", "VIQ7i"],
            ["Bh", "5xXvjdP"],
            ["iD8", "mWv"],
            ["y", "Rl"],
            ["4hNg9knLEx", "EM"],
            ["FyBpy7yXY", "IsKP"],
            ["wzHaHBAiK", "ZE6sX1Mm"],
            ["QWtlbzfi", "ofS5y1m2E"],
            ["jH0uyKjWsI", "eaMwRBOp"],
            ["Q6Se9", "xpJZ"],
            ["OwNluDrBaF", "FGBacPkbQ6"],
            ["tUcKOz", "MZ0qR"],
            ["AGnA8B8AZ", "XcjX8"],
            ["uPxUs", "m6DDm"],
            ["sx4qACI", "X6W60M"],
            ["fb", "S3z"],
            ["SuDg", "obh7"],
            ["L", "Nd9"],
            ["s", "EIekogu6"],
            ["okDK2G4AY", "I7"],
            ["FOFYxI", "hL"],
            ["G", "hZczOONwRM"],
            ["Ufdy0n", "JaayA"],
            ["3C", "0Ttw"],
            ["yeVEK", "It"],
            ["bqA1Q5w", "L5KSOHoqpj"],
            ["Uny", "SuO"],
            ["NBP", "tdF2AYqB"],
            ["XWRN", "3"],
            ["WosSP6wU", "3k7"],
            ["eH", "yVyH4Ess"],
            ["2dl", "C4s7ROXt"],
            ["Eh2x", "vOHo"],
            ["mz", "8"],
            ["Ai", "72eM3kmty"],
            ["DK", "d"],
            ["F0R0E", "usgDBjGWH"],
            ["FSS", "Z"],
            ["IFT9", "5Qn376Z8"],
            ["ywZ2pi", "YhXP"],
            ["TERE8D", "bcXNHlo"],
            ["rhM9Mq55aN", "Mgf5ZxXJNt"],
            ["mYb4MKT", "42"],
            ["kR", "3biyks"],
            ["skIurA", "MWln"],
            ["6nAtyj", "n"],
            ["DUy", "1jGKdHx"],
            ["N", "nHR"],
            ["wBabbmPTN", "uSQ"],
            ["BFgq", "TC"],
            ["sJvlSWoQh", "pAKrG"],
            ["C8IF", "fe51a"],
            ["dgR4lW", "8aW"],
            ["LNcI", "yg90va"],
            ["Vd8MxEmG9V", "bi"],
            ["ZCoUU", "U1qe"],
            ["IU6", "qwd"],
            ["sNC6", "L"],
            ["xg", "n5ty"],
            ["WkAaWN4U", "0sX8ltmsG"],
            ["m5Sn8qC9", "hCC1vJsffO"],
            ["0AxXUuYX", "fmFtbxo"],
            ["sQyRMy", "EtGyB"],
            ["kywzvaU", "YK0kGtK7"],
            ["fe453Zt9E", "cH"],
            ["bgC4H0", "x5dN"],
            ["60", "5mVx516"],
            ["QBB9U", "P"],
            ["BuPmVDj", "P"],
            ["c9YB4FhA", "pIanWmG16"],
            ["qTHrVR", "0aMrWiG"],
            ["OwD0TWNKoO", "2gQJr6"],
            ["gmzv5", "Y5"],
            ["u", "mf2"],
            ["m", "6dJl9Gh8"],
            ["jjMSFSvS4", "tltO7BgCD9"],
            ["ts", "PYMuCI3Tv4"],
            ["j2hVFD7ej", "53oeyvEERz"],
            ["C1xbp6z9", "7"],
            ["l", "J2WNSZl12"],
            ["gAfAgw", "of6d0"],
            ["59sGdsM", "PsLd"],
            ["Mfzg6", "ylqri2o"],
            ["SLvfF3", "Dc"],
            ["p", "E"],
            ["yTg", "FYQLX"],
            ["e1Li", "NQv"],
            ["j3z", "oKse"],
            ["Q1iDjN3y5", "fizd"],
            ["SsqyUG2C", "iyvshj"],
        ]

        # Replacing again with a list of pattern
        for i in replace:
            self.data = self.data.replace(i[0], i[1])

        # Do the formatation
        self.data = self.data + "$" + self.salt + "$" + self.timestamp + "$"

        # Shift the string of lenght of salt - timestamp * length
        i = 0
        while i <= self.length * self.salt.__len__() ** self.difficulty:
            # Shift the string
            self.data = self.data[1:] + self.data[0]
            i += 1

        # If salt is numric
        if self.salt.isnumeric():
            # gcd
            self.gcd = self.difficulty % self.salt

            # Final shift algorithm: Shift by gcd * length ** difficulty
            i = 0
            while i <= self.length * self.gcd * self.difficulty:
                # Shift the string
                self.data = self.data[1:] + self.data[0]
                i += 1

        # Split in 5 char
        self.data = [self.data[i : i + 3] for i in range(0, len(self.data), 3)]

        # Exchange the first and last element
        self.data[0], self.data[-1] = self.data[-1], self.data[0]

        # Convert the list of string in a string
        self.data = "".join(self.data)
        return base64.b64encode(self.data.encode("utf-8")).decode("utf-8")


hasdh = SAHF_512("a", 20)
print(hasdh.hash())
