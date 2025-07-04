"""
系统配置文件
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Milvus配置
MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "finance_knowledge")

# Ollama配置
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://106.52.6.69:11434")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://106.52.6.69:11434")  # Docker环境变量
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-r1:14b")

# 如果设置了OLLAMA_HOST，优先使用它
if OLLAMA_HOST and OLLAMA_HOST != "http://106.52.6.69:11434":
    OLLAMA_BASE_URL = OLLAMA_HOST

# 向量数据库配置
EMBEDDING_DIM = 1024  # BAAI/bge-large-zh-v1.5的嵌入维度
EMBEDDING_MODEL = "BAAI/bge-large-zh-v1.5"

# Web UI配置
WEB_HOST = os.getenv("WEB_HOST", "0.0.0.0")
WEB_PORT = int(os.getenv("WEB_PORT", "5000"))
WEB_DEBUG = os.getenv("WEB_DEBUG", "False").lower() == "true"
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB

# 文件处理配置
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'md', 'pptx', 'txt'}
MAX_TEXT_LENGTH = 1000  # 文本块最大长度
SIMILARITY_THRESHOLD = 0.8  # 相似度阈值

# 重试配置
MAX_RETRIES = 3
RETRY_DELAY = 2

# 日志配置
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/rag_system.log")

# 数据目录配置
DATA_DIR = os.getenv("DATA_DIR", "data")
UPLOADS_DIR = os.getenv("UPLOADS_DIR", "uploads")
EXPORTS_DIR = os.getenv("EXPORTS_DIR", "data/exports") 