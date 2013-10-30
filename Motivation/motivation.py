# -*- coding: utf-8 -*-
import random 

quotes =  ['Life is 10 percent what happens to me and 90 percent of how I react to it. ~ John Maxwell',
            'Your future is created by what you do today ~ Unknown',
             'Happiness cannot be traveled to, owned, earned, or worn. It is the spiritual experience of living every minute with love, grace & gratitude.- Denis Waitley', 
             'The best revenge is massive success ~ Frank Sinatra', 
              'I am thankful for all of those who said NO to me. Its because of them I am doing it myself. ~ Albert Einstein',
               'Build your own dreams, or someone else will hire you to build theirs. ~ Farrah Gray', 
               'Whatever the mind of man can conceive and believe, it can achieve ~ Napoleon Hill', 
               'The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. ~ Joel Brown',
               'You miss 100 percent of the shots you do not take. ~ Wayne Gretzky', 
               'I have missed more than 9000 shots in my career. I have lost almost 300 games. 26 times, I have been trusted to take the game winning shot and missed. I have failed over and over and over again in my life. And that is why I succeed',
                'Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence. ~ Helen Keller',
                'If I have seen further it is by standing on the shoulders of Giants - Sir Isaac Newton',
                'A clever person solves a problem. A wise person avoids it. ~ Albert Einstein'
                ]

i = random.randrange(0, len(quotes))
print quotes[i]