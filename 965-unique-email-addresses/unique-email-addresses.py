class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        k = set()

        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")[0]
            local = local.replace(".", "")

            k.add(local + "@" + domain)

        return len(k)