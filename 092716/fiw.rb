#This is a program that converts numbers to written words for bank transactions.

# create a hundreds method that converts the number to base 10 

def to_hundreds(num)
	in_words = ""
	num_to_words = Hash.new(0)
	num_to_words = { 1=>"One",2=>"Two",3=>"Three",4=>"Four",5=>"Five",6=>"Six",7=>"Seven",8=>"Eight",9=>"Nine",10=>"Ten",11=>"Eleven",12=>"Twelve",13=>"Thirteen",14=>"Fourteen",15=>"Fifteen",16=>"Sixteen",17=>"Seventeen",18=>"Eighteen",19=>"Nineteen",20=>"Twenty",30=>"Thirty",40=>"Fourty",50=>"Fifty",60=>"Sixty",70=>"Seventy",80=>"Eighty",90=>"Ninety" }

	if num / 100 > 0
		in_words = num_to_words[num / 100] + " Hundred "

		if num % 10 != 0
			in_words = in_words + "and "
		end
		num = num % 100
	end

	if num / 10 > 0
		if num / 10 == 1
			in_words = in_words + num_to_words[num] + " "
		elsif num % 10 == 0
			in_words = in_words + num_to_words[num]
		else
			in_words = in_words + num_to_words[num / 10*10] + " " + num_to_words[num % 10]
		end
	elsif num == 0
		in_words
	else 
		in_words = in_words + num_to_words[num]
	end

	in_words
end

def fiw(num)
	in_words = ""

	if num == 0
        return "Zero"
    end

    if num / (10**9) > 0

        in_words = to_hundreds(num / (10**9) ) + " Billion "

        if num / (10**8) == 0
            in_words = words + "and "
        end

        num = num % (10**9)
    end

    if num / (10**6) > 0

        in_words = in_words + to_hundreds(num / (10**6) ) + " Million "

        if num / (10**5) == 0
            in_words = in_words + "and "
        end

        num = num % (10**6)
    end

    if num / (10**3) > 0

        in_words = in_words + to_hundreds(num / (10**3) ) + " Thousand "
        
        if num % (10**2) !=0
            in_words = in_words
        end

        num = num % (10**3)
    end

    if num / (10**2) > 0
        in_words = in_words + to_hundreds(num)
    else
        in_words = in_words + to_hundreds(num)
    end
end
