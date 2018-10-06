def output_log(out):
    f = open('log.txt', 'a')
    st = out + ' \r'
    f.write(st)
    f.close()
