#! -*- coding: utf-8 -*-

import csv
import argparse

def read_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding = "utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def seek_status(csv, keys):
    stats = {}
    for record in csv[1:]:
        comb = [""] * len(keys) # �V���������\(����)
        for i, c in enumerate(record[1:]):
            # ���������󂶂�Ȃ��ꍇ�A�V���������\�ɓ]�L����
            if "" != c:
                # �V���{�����X�g����Y�������������ڂ��T��
                # �V���{�����X�g�ɂ͑S�ẴV���{��������̂ŁA������Ȃ��ꍇ�̃G���[�����͕s�v(�̂͂�)
                idx = keys.index(csv[0][i+1])
                comb[idx] = c
                #print("[DEBUG]: {0}: {1}".format(idx, csv[0][i+1]))
        stats[record[0]] = comb
    return stats

def merge_csv(csv1, csv2):

    # 2��csv�w�b�_�ɑ��݂���V���{�����X�g������
    # �󗓂͏��O����
    keys = []
    [keys.append(elm) for elm in csv1[0] + csv2[0] if (elm not in keys) and ("" != elm)]

    # �ecsv�̏����\��V�����V���{�����X�g�ɑΉ�����悤��蒼��
    stats = {}
    stats.update(seek_status(csv1, keys))
    stats.update(seek_status(csv2, keys))

    return keys, stats
        



def cmdargs ():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv1")
    parser.add_argument("csv2")
    return parser.parse_args()

def main (args):
    csv1 = read_csv(args.csv1)
    csv2 = read_csv(args.csv2)
    keys, stats = merge_csv(csv1, csv2)

    print(",{0}".format(",".join(keys)))
    for stat in stats.keys():
        print("{0},{1}".format(stat, ",".join(stats[stat])))

if __name__ == "__main__":
    main(cmdargs())

