'''
Author: nicho-UJN nicholas9698@outlook.com
Date: 2024-03-13 15:47:25
LastEditors: nicholas9698 nicholas9698@outlook.com
LastEditTime: 2024-09-20 18:05:02
FilePath: /clash_rule_trans/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import re
import argparse
import yaml
import subprocess

parser = argparse.ArgumentParser(prog='Clash Rules Transformer', 
                                 description='Transform the clash configuration file, using the RULE-SET provided by Loyalsoldier/clash-rules', 
                                 epilog='Enjoy the program! :)')

parser.add_argument('-d', '--download', action="store_true", help='Only download the Loyalsoldier/clash-rules')
parser.add_argument('-f', '--file', type=str, dest='file', help='The file_path / sub_url of the clash configuration file')
parser.add_argument('-o', '--outpath', type=str, dest='dir', help='The directory path to save the output files', required=True)

args = parser.parse_args()


def download_rules(save_path: str = './config/'):
    '''
    下载Provider对应的rule集合

    Args:
        save_path(str): 要保存到的文件夹路径
    '''
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    root_path = os.path.abspath(os.path.dirname(__file__))
    
    with open('./config/rules.yaml', 'r') as f:
        rules = yaml.safe_load(f)['rule-providers']

    for rule in rules:
        url = rules[rule]['url']
        rule_name = url.split('/')[-1].split('.')[0]
        command = ['wget', '-O', os.path.join(root_path, save_path) + '/' + rule_name + '.yaml', url]
        try:
            subprocess.run(command, check=True)
            print(f"{rule_name} 下载成功")
        except subprocess.CalledProcessError as e:
            print(f"{rule_name} 下载失败")
            print(e)

if __name__ == '__main__':
    if args.download:
        download_rules(args.dir)
    if args.file: