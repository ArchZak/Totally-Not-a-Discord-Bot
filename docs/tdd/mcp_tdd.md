# TNAB Technical Design Document

**Author:** Aarash Zakeri\
**Date:** 05/07/2026\
**Status:** Draft\
**Project:** Totally Not a Bot MCP

Totally not a bot is going to be an MCP to allow agentic AIs to serve as smart enforcement for discord servers alongside server staff

Note that this TDD is not aligned with the current design philosphies of the project, and that I didn't know some things then. A lot of the learning was done via trial by fire. 

## Problem

### Goals

Want to standardize methods for AI agents to moderate and interact in servers alongside server staff. The idea would be that LLMs can retrieve and analyze message history, send messages, customize profiles, dispense punishment or temporary punishment, etc. Permissions can also be granted to give temporary punishments via silencing. The approach would be designed so that AI agents can regulate multiple servers by setting up oauth passwords via discord bot tokens. So entry to the server will log a bot online, and then make associations with the server. 

### Non-Goals

This approach is based on standardization of security and has nothing to do with the actual AI agent. Methods will be designed to enable MOBILITY across the servers, allow analysis and scraping of channels, and customization of the profile, such that another person can set up their agent, and then decide to either leave them to be fully autonomous in their server, or query the LLM.

AI agent behavior is independent of the MCP project, so staff preferences, reporting, and other prompt / generation handling is out of the scope of this project. 

For now, will gear the project towards moderation, and will consider support for bots to act as normal members later once all the tools, prompts, and resources are set up.

## Proposed Solution

### High-Level Approach

A FastMCP server will act as an API to follow the handler -> services. The MCP will be expected to be used locally as is the current expectation of them anyway. So this would bridge the LLM to any bot it needs to connect to.

This means the tokens are already supplied locally, and the bot will either stay connected to one bot or swap between many. As it's local, the MCP doesn't need to be secured.

There will then be implementations of all the relevant methods required for an agent to interact in a server like any human moderator could. 

So a user would add whatever bot to their server, provide the token to an AI, and then an AI can log into the MCP using that token, where the server would validate that this token actually puts a bot online or not. Security is imperative here. 

### Architecture

Would follow recommended fastmcp structure for entry, tool, resource, prompt directory.

```
tnb_mcp_server/
|-- src/
|   `-- my_server/
|       |-- __init__.py
|       |-- server.py
|       |-- tools/
|       |-- resources/
|       |-- prompts/
|       |-- config/
|       `-- internals/
|           `-- services/
|-- tests/
|-- pixi.toml
`-- documentation.md
```

### MCP Design

### Message Tools

tnb/messages/recent - fetch recent messages (default 20)  
  params: channel_id, limit?, since?, before?

tnb/messages/filter - keyword / structured search (like Discord search)  
  params: query, user_id?, channel_id?, since?, limit?

tnb/messages/pins - fetch all pinned messages in a channel  

tnb/messages/window - fetch a message + surrounding messages (for context windows)  
  params: message_id, before?, after?

tnb/messages/thread - fetch replies / thread for a message  

tnb/messages/activity - aggregate stats (message count, top users, frequency)  
  params: channel_id, since?

tnb/messages/send - send text message (optional reply_to)  

tnb/messages/edit - edit existing message  

tnb/messages/embed - send embed (optional reply_to)  

tnb/messages/delete - delete message  

tnb/messages/react - add reaction  

tnb/messages/unreact - remove own reaction  

tnb/messages/bulk_delete - delete multiple messages at once  
  params: channel_id, message_ids? | count?

### Channel Tools

tnb/channels/list - fetch all channels + descriptions + ids in server

tnb/channels/by_category - fetch channels in a category  
  params: category_id  

tnb/channels/activity - channel activity stats to detect usage

tnb/channels/dead - detect inactive channels  
  params: threshold_days

tnb/channels/create - create channel  
  params: name, type (text/voice/forum), category_id?

tnb/channels/edit - edit channel settings  

tnb/channels/delete - delete channel  

tnb/channels/move - move channel to another category

### Category Tools

tnb/categories/list - fetch all categories and their channels

tnb/categories/create - create category  

tnb/categories/edit - edit category  

tnb/categories/delete - delete category

### Profile Tools

tnb/profile/status - set status

tnb/profile/about - set about me

### User Tools

tnb/users/id - resolve user id  

tnb/users/profile - basic profile + roles + join date  

tnb/users/activity - message activity stats  
  params: since?

tnb/users/infractions - past moderation actions on user

tnb/users/dm - send direct message  

tnb/users/rename - change user nickname

### Role Tools

tnb/roles/list - get all roles + info

tnb/roles/by_id - fetch role details by id

tnb/roles/assign - assign role to user  

tnb/roles/remove - remove role from user  

tnb/roles/create - create new role  

tnb/roles/delete - delete role  

tnb/roles/bulk_assign - assign role to multiple users

### Enforcement Tools

tnb/enforcement/warn - warn user (no restriction)  

tnb/enforcement/silence - 10 min mute

tnb/enforcement/mute - mute with custom duration  

tnb/enforcement/kick - remove user from server  

tnb/enforcement/ban - ban user  

tnb/enforcement/delete_messages - remove messages (targeted or bulk)  

tnb/enforcement/rename - force nickname change  

tnb/enforcement/move_voice - move user between voice channels  

tnb/enforcement/disconnect_voice - disconnect user from vc

### Moderation (Decision Layer) 

Meant to combine steps 

tnb/moderation/evaluate - analyze message(s) for spam, toxicity, abuse  
  params: message_id | text  
  returns: spam_score, toxicity_score, flags, recommended_action

tnb/moderation/auto_enforce - call evaluate ^^ + respective action in one step, kind of like ISR in OS -> make a punishment suggestion system
  params: message_id | user_id, policy?  
  returns: action_taken, reasoning

### Message Streamlining (Decision Layer)

tnb/messages/summary - summarize messages over a window  
  params: channel_id, since? | limit?

tnb/messages/semantic_search - embedding-based search (not keyword)  
  params: query, channel_id?, limit?

### User Tracking (Decision Layer)

tnb/users/risk - evaluate user risk based on past infractions nad notes  
  params: user_id  
  returns: risk_score, reasons

tnb/users/summary - summarize user behavior  
  params: user_id, since?

### Channel Overview

tnb/channels/summary - summarize what a channel is used for  
  params: channel_id, since?

tnb/channels/recommend - suggest actions (archive, reorganize, etc.)  
  params: channel_id?

### General Server Resources

tnb/server/emojis - fetch all emojis  

tnb/server/info - basic server metadata  

tnb/server/invites - active invite links

## Blockers


## Testing Plan

If given to 5 LLMs, they should all act the same. if they dont then the interface is bad

## Alternative Approaches

### Alternative 1
