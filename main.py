def medians(nums1, nums2):
    new_num = nums1 + nums2
    new_num.sort()
    length = len(new_num)

    if length % 2 ==0:
        median = (new_num[int(length/2-1)] + new_num[int(length/2)])/2
        #берем сложение среднего левого и правого чисел потому что длина списка четная
        #учитывая что в списке индекс с 0
    else:
        median = new_num[int(length+1/2 - 1)] #при нечетной длине, чтобы получить нужный целый индекс
                                              #пришлось довести до четного и уменьшить на единицу
                                              #потому что в списке с 0 индекса идет счет
    return(median)
