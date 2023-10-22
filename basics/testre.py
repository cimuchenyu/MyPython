import re

sentence = '''
void DynamicProperty::getPropertyList(std::vector<Property*> &List) const {
    for (auto &v : props.get<0>())
        List.push_back(v.property);
}

const char* DynamicProperty::getPropertyDocumentation(const char *name) const
{
    auto &index = props.get<0>();
    auto it = index.find(name);
    if (it != index.end())
        return it->doc.c_str();
    return nullptr;
}

Property* DynamicProperty::addDynamicProperty(PropertyContainer &pc, const char* type,
        const char* name, const char* group, const char* doc, short attr, bool ro, bool hidden)
{
    if(!type)
        type = "<null>";
'''
#sentence_list = re.split(r'{', sentence)
#print(sentence_list)
aa= re.sub(r'.*::.*{',r'\g<0> ' + '-- \r\n added text', sentence, flags=re.IGNORECASE| re.MULTILINE|re.DOTALL)
print(aa)

# pattern = re.compile(r'.*::.*{',flags=re.IGNORECASE| re.MULTILINE|re.DOTALL)
# bb = re.findall(pattern, sentence)
# print(bb)

