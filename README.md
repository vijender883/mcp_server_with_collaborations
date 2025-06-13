# MCP Server Setup Guide

This guide will help you set up and configure MCP (Model Context Protocol) servers for use with Cursor IDE.

## Prerequisites

- Python 3.8 or higher
- Node.js and npm (for firecrawl server)
- Cursor IDE
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/vijender883/mcp_server_with_collaborations
cd mcp_server_with_collaborations
```

### 2. Create a Virtual Environment

#### Windows CMD

```cmd
python -m venv venv
venv\Scripts\activate
```

#### Windows PowerShell

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**PowerShell Troubleshooting:**
If you encounter an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating the virtual environment again.

#### macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Cursor IDE Configuration

### 1. Install and Open Cursor

1. Download Cursor from [cursor.sh](https://cursor.sh)
2. Install and open Cursor
3. Navigate to **Settings** → **MCP Tools**

### 2. Configure MCP Servers

Create or edit your `mcp.json` configuration file with one of the following setups:

## Configuration Examples

### MCP-text-analysis Server Only

```json
{
  "mcpServers": {
    "MCP-text-analysis": {
      "command": "path to your virtual env Python, e.g., /home/user001/Desktop/work3/mcp_server_with_collaborations/venv/bin/python3",
      "args": ["absolute path to mcp_server.py"],
      "host": "127.0.0.1",
      "port": 8080,
      "timeout": 30000
    }
  }
}
```

**Note:** Replace the paths with your actual system paths:
- **Windows**: `C:\Users\YourUsername\path\to\project\venv\Scripts\python.exe`
- **macOS/Linux**: `/home/username/path/to/project/venv/bin/python3`

### mcp-server-firecrawl Only

```json
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-xxxxxxxxxxxxxxx"
      }
    }
  }
}
```

**Note:** Replace `fc-xxxxxxxxxxxxxxx` with your actual Firecrawl API key.

### Combined Setup (Both Servers)

```json
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-xxxxxxxxxxxxxxx"
      }
    },
    "MCP-text-analysis": {
      "command": "path to your virtual env Python",
      "args": ["absolute path to mcp_server.py"],
      "host": "127.0.0.1",
      "port": 8080,
      "timeout": 30000
    }
  }
}
```

## Finding Your Paths

### Virtual Environment Python Path

After activating your virtual environment, you can find the Python path:

**Windows:**
```cmd
where python
```

**macOS/Linux:**
```bash
which python3
```

### MCP Server Script Path

Use the absolute path to your `mcp_server.py` file. For example:
- **Windows**: `C:\Users\YourUsername\Desktop\project\mcp_server.py`
- **macOS/Linux**: `/home/username/Desktop/project/mcp_server.py`

## API Keys

### Firecrawl API Key

1. Sign up at [Firecrawl](https://firecrawl.dev)
2. Get your API key from the dashboard
3. Replace `fc-xxxxxxxxxxxxxxx` in the configuration with your actual key

## Testing the Setup

1. Save your `mcp.json` configuration
2. Restart Cursor IDE
3. The MCP servers should now be available in Cursor's tools menu

## Troubleshooting

### Common Issues

1. **Python path not found**: Ensure you're using the absolute path to the Python executable in your virtual environment
2. **Permission denied**: On Windows, try running Cursor as administrator
3. **Port conflicts**: If port 8080 is in use, change it to another port (e.g., 8081)
4. **API key errors**: Verify your Firecrawl API key is correct and has sufficient credits

### Verification

To verify your setup is working:
1. Check Cursor's MCP Tools settings to see if servers are connected
2. Look for any error messages in the Cursor console
3. Test the MCP functionality within Cursor

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [Cursor IDE Documentation](https://cursor.sh/docs)
- [Firecrawl Documentation](https://docs.firecrawl.dev)

## Support

If you encounter issues, please check the troubleshooting section above or refer to the project's issue tracker.