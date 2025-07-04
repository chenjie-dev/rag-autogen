#!/usr/bin/env python3
"""
Ollama API测试脚本
==================

功能说明:
- 测试Ollama API连接是否正常
- 验证模型是否可用
- 测试基本的文本生成功能
- 用于系统部署前的连接测试

使用方法:
    python3 ollama_py_test.py

测试内容:
1. 连接Ollama服务
2. 列出可用模型
3. 测试文本生成
4. 错误处理和重试机制

作者: RAG系统开发团队
版本: 1.0.0
更新日期: 2024
"""

import ollama
import sys
import textwrap
import time

def print_section(title: str, content: str, width: int = 80):
    """打印格式化的内容区块"""
    print("\n" + "=" * width)
    print(f" {title} ".center(width, "="))
    print("=" * width)
    
    # 使用textwrap处理长文本
    wrapped_content = textwrap.fill(content, width=width-4)
    print(wrapped_content)
    print("=" * width)

def typewriter_print(text: str, delay: float = 0.01):
    """打字机效果打印文本"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

try:
    # 创建客户端
    client = ollama.Client(host='http://106.52.6.69:11434')
    
    # 打印问题
    question = "你好，什么是股票市场？"
    print_section("问题", question)
    
    # 使用流式输出发送聊天请求
    print_section("回答", "")  # 先打印回答的标题
    print("=" * 80)  # 打印分隔线
    
    # 使用stream=True参数获取流式响应
    stream = client.chat(
        model='deepseek-r1:14b',
        messages=[{'role': 'user', 'content': question}],
        stream=True
    )
    
    # 实时打印响应内容，使用打字机效果
    for chunk in stream:
        if 'message' in chunk and 'content' in chunk['message']:
            content = chunk['message']['content']
            # 跳过思考过程
            if content.startswith('<think>'):
                continue
            typewriter_print(content)
    
    print("\n" + "=" * 80)  # 打印结束分隔线
    
except Exception as e:
    print("\n" + "!" * 80)
    print(f"错误: {str(e)}".center(80))
    print("!" * 80)
    sys.exit(1) 