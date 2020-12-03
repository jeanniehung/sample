from mysample.sample_dir.sample import Sample


if __name__ == '__main__':
    sample = Sample()
    print(sample.insert([12, 2, 3, 45, 6]))
    sample.combination('AJKB')
    print(sample.count('ghhauahhaaiw'))
    print(sample.count2('bhshuabhsv'))
    sample.duplicate_removal('ghkhakzbcaosss')
    print(sample.duplicate_removal2('bkhkjasjahj'))
    sample.is_prime_number(22)
    print(sample.print_prime_numbers(100))
    sample.palindrome2('nbhthbn')
    print(sample.print_palindrome_num())
    sample.find_longest_palindrome_num('hhkkjshdiuish')
    sample.change('hhGUSDHAGahjksabc')
    print(sample.random_distribution_gift())


























