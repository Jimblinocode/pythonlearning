greeting = "hello world!"
hello = greeting
howdy = hello




num = 2
nums = [2, 6, 7, 14]
nums2 = nums
nums3 = nums.copy()

if hello is greeting is howdy:
        if num is not nums is not greeting:
            if nums is nums2 is not nums3:
                print("Correct!")
