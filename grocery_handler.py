import os

GROCERY_FILE = "grocerylist.txt"

async def handle_add_gl(message):
    content_upper = message.content.upper()
    split_index = content_upper.find("ADD GL") + len("ADD GL")
    item_text = message.content[split_index:].strip()

    if item_text:
        try:
            with open(GROCERY_FILE, "a", encoding="utf-8") as f:
                f.write(item_text + "\n")
            await message.channel.send(f"✅ Added to grocery list: `{item_text}`")
        except Exception as e:
            await message.channel.send("⚠️ Error writing to grocery list.")
            print(f"Error: {e}")
    else:
        await message.channel.send("❗ Nothing to add. Please provide a grocery item.")


async def handle_remove_gl(message):
    content_upper = message.content.upper()
    split_index = content_upper.find("REMOVE GL") + len("REMOVE GL")
    item_text = message.content[split_index:].strip()

    if not os.path.exists(GROCERY_FILE):
        await message.channel.send("🗒️ Grocery list is empty.")
        return

    if not item_text:
        await message.channel.send("❗ Please specify what to remove.")
        return

    try:
        with open(GROCERY_FILE, "r", encoding="utf-8") as f:
            items = [line.strip() for line in f if line.strip()]

        if item_text not in items:
            await message.channel.send(f"❌ Item `{item_text}` not found in grocery list.")
            return

        items.remove(item_text)
        with open(GROCERY_FILE, "w", encoding="utf-8") as f:
            for item in items:
                f.write(item + "\n")

        await message.channel.send(f"🗑️ Removed `{item_text}` from grocery list.")
    except Exception as e:
        await message.channel.send("⚠️ Error removing item.")
        print(f"Error: {e}")


async def handle_show_gl(message):
    if not os.path.exists(GROCERY_FILE):
        await message.channel.send("🗒️ Grocery list is empty.")
        return

    try:
        with open(GROCERY_FILE, "r", encoding="utf-8") as f:
            items = [line.strip() for line in f if line.strip()]

        if not items:
            await message.channel.send("🗒️ Grocery list is empty.")
            return

        grocery_list = "\n".join(f"- {item}" for item in items)
        await message.channel.send(f"🛒 **Grocery List:**\n{grocery_list}")
    except Exception as e:
        await message.channel.send("⚠️ Error reading grocery list.")
        print(f"Error: {e}")


async def handle_clear_gl(message):
    try:
        open(GROCERY_FILE, "w").close()  # Empty the file
        await message.channel.send("🧹 Grocery list cleared.")
    except Exception as e:
        await message.channel.send("⚠️ Error clearing grocery list.")
        print(f"Error: {e}")

async def handle_help_gl(message):
    commands = list(COMMAND_MAP.keys())
    commands.sort()
    help_text = "📋 **Available Grocery List Commands:**\n"
    for cmd in commands:
        help_text += f"- `{cmd}`\n"
    await message.channel.send(help_text)

COMMAND_MAP = {
    "ADD GL": handle_add_gl,
    "REMOVE GL": handle_remove_gl,
    "SHOW GL": handle_show_gl,
    "CLEAR GL": handle_clear_gl,
    "HELP GL": handle_help_gl
}
