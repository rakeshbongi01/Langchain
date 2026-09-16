from langchain_community.tools import ShellTool

shell_tool = ShellTool()
run= shell_tool.invoke("whoami")
print(run)