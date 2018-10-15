class Card 
{
    public:
        int mark;  // 0-normal 1-restraint 2-resistance
        int type;  // 0-quick 1-arts 2-buster
        int priority;
        bool buster;
        float atk;

        void get_atk()
        {
            // setting basic card type
            switch(type)
            {
                case 0: atk = 0.8;
                        break;
                case 1: atk = 1.0;
                        break;
                case 2: atk = 1.5;
                        break;
            };
            // setting priority attack gain
            switch(priority)
            {
                case 1: atk = atk * 1.2;
                        break;
                case 2: atk = atk * 1.4;
                        break;
            };
            // setting buster gain
            if(buster == 1)
                atk += 0.5;
            // setting restraint and resistance
            switch(mark)
            {
                case 1: atk = atk * 2;
                        break;
                case 2: atk = atk * 0.5;
                        break;
            }
        }
};