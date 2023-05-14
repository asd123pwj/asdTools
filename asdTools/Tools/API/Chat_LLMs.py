from asdTools.Classes.API.LLMsAPI import LLMsAPI


if __name__ == "__main__":
    url = "http://localhost:8000"
    print("Support command:")
    print("\exit: Terminate chating.")
    ChatBot = LLMsAPI(url)
    ChatBot.chating()